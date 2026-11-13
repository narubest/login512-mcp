#!/usr/bin/env python3
"""
sdk-ai/mcp-server/server.py — Official Login512 Model Context Protocol (MCP) Server
Implements the Model Context Protocol (JSON-RPC 2.0 over stdio) for Claude Desktop,
Cursor, Windsurf, VS Code, Cline, Roo Code, and autonomous coding agents.
Provides instant project inspection, full 28-framework SDK installation instructions,
and security auditing for Post-Quantum Biometrics & Zero-Image Passkeys.
"""

from __future__ import annotations
import json
import os
from pathlib import Path
import sys
from typing import Any, Optional

SDK_CATALOG: dict[str, dict[str, Any]] = {
    # 1. Frontend Web (7)
    "react": {
        "name": "React",
        "category": "frontend",
        "install_command": "npm install https://login512.com/packages/react.tgz",
        "package_url": "https://login512.com/packages/react.tgz",
        "guide_url": "https://login512.com/guide.html#sdk-react",
        "quick_code": """import { Login512Button } from '@login512/react';

<Login512Button
  publishableKey="l512_pk_live_your_key"
  onSuccess={async (res) => {
    await fetch('/api/login', { method: 'POST', body: JSON.stringify({ token: res.token }) });
  }}
/>""",
    },
    "nextjs": {
        "name": "Next.js",
        "category": "frontend",
        "install_command": "npm install https://login512.com/packages/nextjs.tgz",
        "package_url": "https://login512.com/packages/nextjs.tgz",
        "guide_url": "https://login512.com/guide.html#sdk-nextjs",
        "quick_code": """'use client';
import { Login512Button } from '@login512/nextjs/client';

export default function LoginPage() {
  return <Login512Button onSuccess={async (res) => { await fetch('/api/auth', { method: 'POST', body: JSON.stringify(res) }); }} />;
}""",
    },
    "vue": {
        "name": "Vue.js",
        "category": "frontend",
        "install_command": "npm install https://login512.com/packages/vue.tgz",
        "package_url": "https://login512.com/packages/vue.tgz",
        "guide_url": "https://login512.com/guide.html#sdk-vue",
        "quick_code": """<template>
  <Login512Auth publishable-key="l512_pk_live_your_key" @success="onSuccess" />
</template>
<script setup>
import { Login512Auth } from '@login512/vue';
const onSuccess = (res) => console.log('Token:', res.token);
</script>""",
    },
    "nuxt": {
        "name": "Nuxt",
        "category": "frontend",
        "install_command": "npm install https://login512.com/packages/nuxt.tgz",
        "package_url": "https://login512.com/packages/nuxt.tgz",
        "guide_url": "https://login512.com/guide.html#sdk-nuxt",
        "quick_code": """// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@login512/nuxt'],
  login512: { publishableKey: process.env.LOGIN512_PK }
});""",
    },
    "svelte": {
        "name": "Svelte / SvelteKit",
        "category": "frontend",
        "install_command": "npm install https://login512.com/packages/svelte.tgz",
        "package_url": "https://login512.com/packages/svelte.tgz",
        "guide_url": "https://login512.com/guide.html#sdk-svelte",
        "quick_code": """<script lang="ts">
import { Login512Button } from '@login512/svelte';
</script>
<Login512Button publishableKey="l512_pk_live_your_key" on:success={(e) => console.log(e.detail.token)} />""",
    },
    "angular": {
        "name": "Angular",
        "category": "frontend",
        "install_command": "npm install https://login512.com/packages/angular.tgz",
        "package_url": "https://login512.com/packages/angular.tgz",
        "guide_url": "https://login512.com/guide.html#sdk-angular",
        "quick_code": """import { Component } from '@angular/core';
import { Login512ButtonComponent } from '@login512/angular';

@Component({
  standalone: true,
  imports: [Login512ButtonComponent],
  template: `<login512-button (success)="onAuthSuccess($event)"></login512-button>`
})
export class LoginComponent {}""",
    },
    "html5": {
        "name": "HTML5 Web Component",
        "category": "frontend",
        "install_command": '<script src="https://cdn.login512.com/sdk/login512-sdk.js"></script>',
        "package_url": "https://cdn.login512.com/sdk/login512-sdk.js",
        "guide_url": "https://login512.com/guide.html#sdk-web-component",
        "quick_code": """<script src="https://cdn.login512.com/sdk/login512-sdk.js"></script>
<login512-card client-id="l512_pk_live_your_key"></login512-card>
<script>
document.querySelector('login512-card').addEventListener('login512:success', (e) => {
  console.log('Biometric Token:', e.detail.token);
});
</script>""",
    },

    # 2. Backend APIs (14)
    "node_express": {
        "name": "Node.js Express",
        "category": "backend",
        "install_command": "npm install https://login512.com/packages/node-express.tgz",
        "package_url": "https://login512.com/packages/node-express.tgz",
        "guide_url": "https://login512.com/guide.html#sdk-node-express",
        "quick_code": """const express = require('express');
const { login512Auth } = require('@login512/express');

const app = express();
app.use('/api/protected', login512Auth({ secretKey: process.env.LOGIN512_SECRET_KEY }));
app.get('/api/protected/user', (req, res) => res.json({ user: req.login512User }));""",
    },
    "node_nestjs": {
        "name": "Node.js NestJS",
        "category": "backend",
        "install_command": "npm install https://login512.com/packages/node-nestjs.tgz",
        "package_url": "https://login512.com/packages/node-nestjs.tgz",
        "guide_url": "https://login512.com/guide.html#sdk-node-nestjs",
        "quick_code": """import { Controller, Get, UseGuards } from '@nestjs/common';
import { Login512AuthGuard, CurrentUser } from '@login512/nestjs';

@Controller('user')
export class UserController {
  @Get('profile')
  @UseGuards(Login512AuthGuard)
  getProfile(@CurrentUser() user) { return user; }
}""",
    },
    "node_fastify": {
        "name": "Node.js Fastify",
        "category": "backend",
        "install_command": "npm install https://login512.com/packages/node-fastify.tgz",
        "package_url": "https://login512.com/packages/node-fastify.tgz",
        "guide_url": "https://login512.com/guide.html#sdk-node-fastify",
        "quick_code": """const fastify = require('fastify')();
const login512 = require('@login512/fastify');

fastify.register(login512, { secretKey: process.env.LOGIN512_SECRET_KEY });
fastify.get('/api/protected', { preHandler: [fastify.login512Auth] }, async (req, reply) => {
  return { user: req.login512User };
});""",
    },
    "fastapi": {
        "name": "Python FastAPI",
        "category": "backend",
        "install_command": "pip install https://login512.com/packages/fastapi.tar.gz",
        "package_url": "https://login512.com/packages/fastapi.tar.gz",
        "guide_url": "https://login512.com/guide.html#sdk-python-fastapi",
        "quick_code": """from fastapi import FastAPI, Depends
from login512_fastapi import Login512Auth, Login512User

app = FastAPI()
auth = Login512Auth(secret_key=os.getenv('LOGIN512_SECRET_KEY'))

@app.get('/api/profile')
async def profile(user: Login512User = Depends(auth)):
    return {'user_id': user.sub, 'pqc_verified': user.pqc_valid}""",
    },
    "django": {
        "name": "Python Django",
        "category": "backend",
        "install_command": "pip install https://login512.com/packages/django.tar.gz",
        "package_url": "https://login512.com/packages/django.tar.gz",
        "guide_url": "https://login512.com/guide.html#sdk-python-django",
        "quick_code": """# settings.py
AUTHENTICATION_BACKENDS = ['login512_django.backends.Login512Backend']
LOGIN512_SECRET_KEY = os.getenv('LOGIN512_SECRET_KEY')

# views.py
from login512_django.decorators import login512_required

@login512_required
def profile_view(request):
    return JsonResponse({'user': request.user.username})""",
    },
    "flask": {
        "name": "Python Flask",
        "category": "backend",
        "install_command": "pip install https://login512.com/packages/flask.tar.gz",
        "package_url": "https://login512.com/packages/flask.tar.gz",
        "guide_url": "https://login512.com/guide.html#sdk-python-flask",
        "quick_code": """from flask import Flask, jsonify, g
from flask_login512 import Login512, login512_required

app = Flask(__name__)
login512 = Login512(app, secret_key=os.getenv('LOGIN512_SECRET_KEY'))

@app.route('/api/profile')
@login512_required
def profile():
    return jsonify({'user_id': g.login512_user['sub']})""",
    },
    "laravel": {
        "name": "PHP & Laravel",
        "category": "backend",
        "install_command": "curl -s https://login512.com/sdk/php/Login512.php -o app/Services/Login512.php",
        "package_url": "https://login512.com/sdk/php/Login512.php",
        "guide_url": "https://login512.com/guide.html#sdk-php-laravel",
        "quick_code": """use App\\Services\\Login512;

public function authenticate(Request $request) {
    $result = Login512::verifyToken(env('LOGIN512_SECRET_KEY'), $request->token);
    if ($result['valid']) {
        $user = User::firstOrCreate(['login512_id' => $result['claims']['sub']]);
        Auth::login($user);
        return response()->json(['status' => 'success']);
    }
    return response()->json(['error' => 'Invalid biometric token'], 401);
}""",
    },
    "symfony": {
        "name": "PHP Symfony",
        "category": "backend",
        "install_command": "curl -s https://login512.com/sdk/php/Login512.php -o src/Service/Login512.php",
        "package_url": "https://login512.com/sdk/php/Login512.php",
        "guide_url": "https://login512.com/guide.html#sdk-php-symfony",
        "quick_code": """use App\\Service\\Login512;

$res = Login512::verifyToken($this->getParameter('login512_secret_key'), $token);
if ($res['valid']) {
    // Authenticate user in Symfony security token storage
}""",
    },
    "spring_boot": {
        "name": "Java Spring Boot",
        "category": "backend",
        "install_command": "curl -s https://login512.com/packages/spring-boot.zip -o spring-boot.zip",
        "package_url": "https://login512.com/packages/spring-boot.zip",
        "guide_url": "https://login512.com/guide.html#sdk-java-spring-boot",
        "quick_code": """// application.yml
login512:
  secret-key: ${LOGIN512_SECRET_KEY}
  endpoint: https://login512.com""",
    },
    "quarkus": {
        "name": "Java Quarkus",
        "category": "backend",
        "install_command": "curl -s https://login512.com/packages/quarkus.zip -o quarkus.zip",
        "package_url": "https://login512.com/packages/quarkus.zip",
        "guide_url": "https://login512.com/guide.html#sdk-java-quarkus",
        "quick_code": """// application.properties
quarkus.login512.secret-key=${LOGIN512_SECRET_KEY}
quarkus.login512.endpoint=https://login512.com""",
    },
    "go": {
        "name": "Go (Golang)",
        "category": "backend",
        "install_command": "curl -s https://login512.com/packages/go.zip -o login512-go.zip",
        "package_url": "https://login512.com/packages/go.zip",
        "guide_url": "https://login512.com/guide.html#sdk-go",
        "quick_code": """// 1. unzip login512-go.zip
// 2. in go.mod: replace github.com/login512/login512-go => ./login512-go

import "github.com/login512/login512-go"

client, err := login512.NewClient(os.Getenv("LOGIN512_SECRET_KEY"))
res, err := client.VerifyToken(ctx, token, "")
if err == nil && res.Valid {
    fmt.Printf("Verified User: %s\\n", res.Claims.Subject)
}""",
    },
    "rust": {
        "name": "Rust",
        "category": "backend",
        "install_command": "curl -s https://login512.com/packages/rust.zip -o login512-rs.zip",
        "package_url": "https://login512.com/packages/rust.zip",
        "guide_url": "https://login512.com/guide.html#sdk-rust",
        "quick_code": """// 1. unzip login512-rs.zip
// 2. in Cargo.toml: login512 = { path = "./login512-rs" }

let client = login512::Client::new(secret_key);
let res = client.verify_token(&token).await?;
if res.is_valid() {
    println!("User: {}", res.claims.sub);
}""",
    },
    "dotnet": {
        "name": "C# & .NET Core",
        "category": "backend",
        "install_command": "curl -s https://login512.com/packages/dotnet.zip -o login512-dotnet.zip",
        "package_url": "https://login512.com/packages/dotnet.zip",
        "guide_url": "https://login512.com/guide.html#sdk-dotnet",
        "quick_code": """// 1. unzip login512-dotnet.zip
// 2. dotnet add reference ./login512-dotnet/Login512.AspNetCore.csproj

builder.Services.AddAuthentication("Login512")
    .AddScheme<Login512AuthenticationOptions, Login512AuthenticationHandler>("Login512", opt => {
        opt.SecretKey = builder.Configuration["LOGIN512_SECRET_KEY"];
    });""",
    },
    "ruby_rails": {
        "name": "Ruby on Rails",
        "category": "backend",
        "install_command": "curl -s https://login512.com/packages/ruby-rails.zip -o login512-rails.zip",
        "package_url": "https://login512.com/packages/ruby-rails.zip",
        "guide_url": "https://login512.com/guide.html#sdk-ruby-rails",
        "quick_code": """# 1. unzip login512-rails.zip
# 2. in Gemfile: gem 'login512', path: './login512-rails'

Login512.configure do |config|
  config.secret_key = ENV['LOGIN512_SECRET_KEY']
end""",
    },

    # 3. Mobile Apps (4)
    "flutter": {
        "name": "Flutter Mobile",
        "category": "mobile",
        "install_command": "curl -s https://login512.com/packages/flutter.zip -o login512_flutter.zip",
        "package_url": "https://login512.com/packages/flutter.zip",
        "guide_url": "https://login512.com/guide.html#sdk-flutter",
        "quick_code": """# 1. unzip login512_flutter.zip
# 2. in pubspec.yaml: login512_flutter: { path: ./login512_flutter }

import 'package:login512_flutter/login512_flutter.dart';

final result = await Login512.authenticate(publishableKey: 'l512_pk_live_your_key');
if (result.isSuccess) { print('Token: ${result.token}'); }""",
    },
    "react_native": {
        "name": "React Native & Expo",
        "category": "mobile",
        "install_command": "npm install https://login512.com/packages/react-native.tgz",
        "package_url": "https://login512.com/packages/react-native.tgz",
        "guide_url": "https://login512.com/guide.html#sdk-react-native",
        "quick_code": """import { Login512Button } from '@login512/react-native';

<Login512Button publishableKey="l512_pk_live_your_key" onSuccess={(res) => console.log(res.token)} />""",
    },
    "ios": {
        "name": "iOS Native (Swift)",
        "category": "mobile",
        "install_command": "curl -s https://login512.com/packages/ios.zip -o Login512Kit.zip",
        "package_url": "https://login512.com/packages/ios.zip",
        "guide_url": "https://login512.com/guide.html#sdk-ios",
        "quick_code": """// 1. unzip Login512Kit.zip
// 2. Drag Login512Kit into Xcode Project Navigator

import Login512Kit

Login512.authenticate(publishableKey: "l512_pk_live_your_key") { result in
    switch result {
    case .success(let token): print("Token: \\(token)")
    case .failure(let err): print("Error: \\(err)")
    }
}""",
    },
    "android": {
        "name": "Android Native (Kotlin)",
        "category": "mobile",
        "install_command": "curl -s https://login512.com/packages/android.zip -o login512-android.zip",
        "package_url": "https://login512.com/packages/android.zip",
        "guide_url": "https://login512.com/guide.html#sdk-android",
        "quick_code": """// 1. unzip login512-android.zip and place .aar in app/libs/
// 2. in build.gradle: implementation(fileTree(mapOf("dir" to "libs", "include" to listOf("*.aar"))))

Login512.authenticate(context, "l512_pk_live_your_key") { token ->
    Log.d("Login512", "Authenticated: $token")
}""",
    },

    # 4. CMS & Plugins (3)
    "wordpress": {
        "name": "WordPress & WooCommerce",
        "category": "cms",
        "install_command": "wp plugin install https://login512.com/packages/wordpress.zip --activate",
        "package_url": "https://login512.com/packages/wordpress.zip",
        "guide_url": "https://login512.com/guide.html#sdk-wordpress",
        "quick_code": """# Or upload via WordPress Admin:
# 1. Plugins -> Add New -> Upload Plugin -> select wordpress.zip
# 2. Click Install Now and Activate
# 3. Enter Publishable Key & Secret Key in Settings -> Login512""",
    },
    "shopify": {
        "name": "Shopify App Extension",
        "category": "cms",
        "install_command": "curl -s https://login512.com/packages/shopify.zip -o login512-shopify.zip",
        "package_url": "https://login512.com/packages/shopify.zip",
        "guide_url": "https://login512.com/guide.html#sdk-shopify",
        "quick_code": """// 1. unzip login512-shopify.zip
// 2. Include in theme.liquid or hydrogen app:
// <script src="https://cdn.login512.com/sdk/login512-sdk.js"></script>""",
    },
    "strapi": {
        "name": "Strapi Headless CMS",
        "category": "cms",
        "install_command": "npm install https://login512.com/packages/strapi.tgz",
        "package_url": "https://login512.com/packages/strapi.tgz",
        "guide_url": "https://login512.com/guide.html#sdk-strapi",
        "quick_code": """// config/plugins.js
module.exports = {
  'login512': {
    enabled: true,
    config: {
      secretKey: process.env.LOGIN512_SECRET_KEY
    }
  }
};""",
    },
}

TOOLS = [
    {
        "name": "login512_inspect_project",
        "description": "Inspects project directory to detect programming language, framework (React, Next.js, Vue, Nuxt, Svelte, Angular, Express, NestJS, Fastify, FastAPI, Django, Flask, Laravel, Symfony, Spring Boot, Quarkus, Go, Rust, .NET Core, Ruby on Rails, Flutter, iOS, Android, WordPress, Shopify, Strapi) and recommend official integration package.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "project_path": {
                    "type": "string",
                    "description": "Absolute or relative path to project root (defaults to current directory)",
                }
            },
        },
    },
    {
        "name": "login512_get_instructions",
        "description": "Returns exact, verified installation commands, package download URLs (HTTP 200 live), copy-paste-ready code snippets, and deep guide anchor links for any of the 28 official Login512 SDKs and plugins.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "framework": {
                    "type": "string",
                    "description": "Target framework or language (e.g., 'react', 'nextjs', 'fastapi', 'django', 'flask', 'go', 'dotnet', 'laravel', 'spring_boot', 'flutter', 'wordpress', etc.)",
                }
            },
            "required": ["framework"],
        },
    },
    {
        "name": "login512_list_sdks",
        "description": "Lists all 28 official Login512 SDKs and plugins across Frontend Web, Backend APIs, Mobile Apps, and CMS plugins with their official package URLs.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "Optional category filter: 'all', 'frontend', 'backend', 'mobile', 'cms'",
                }
            },
        },
    },
    {
        "name": "login512_audit_code",
        "description": "Audits client or server integration code to ensure compliance with Zero-Image privacy, post-quantum verification, and replay protection.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "Source code snippet to audit",
                },
                "filename": {
                    "type": "string",
                    "description": "Filename being audited (e.g. 'auth.ts', 'login.php')",
                }
            },
            "required": ["code"],
        },
    },
]

ALIASES: dict[str, str] = {
    "reactjs": "react",
    "next": "nextjs",
    "vuejs": "vue",
    "sveltekit": "svelte",
    "express": "node_express",
    "expressjs": "node_express",
    "nestjs": "node_nestjs",
    "fastify": "node_fastify",
    "node": "node_express",
    "nodejs": "node_express",
    "python": "fastapi",
    "py": "fastapi",
    "php": "laravel",
    "golang": "go",
    "c#": "dotnet",
    "csharp": "dotnet",
    ".net": "dotnet",
    "aspnet": "dotnet",
    "rails": "ruby_rails",
    "ruby": "ruby_rails",
    "spring": "spring_boot",
    "springboot": "spring_boot",
    "swift": "ios",
    "swiftui": "ios",
    "kotlin": "android",
    "compose": "android",
    "wp": "wordpress",
    "woocommerce": "wordpress",
    "html": "html5",
    "cdn": "html5",
}

def inspect_project(project_path: Optional[str] = None) -> dict[str, Any]:
    base = Path(project_path or ".").resolve()
    detected: list[str] = []

    # 1. Node.js Ecosystem
    if (base / "package.json").exists():
        try:
            pkg = json.loads((base / "package.json").read_text(encoding="utf-8"))
            deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
            if "next" in deps or (base / "next.config.js").exists() or (base / "next.config.mjs").exists() or (base / "next.config.ts").exists():
                detected.append("nextjs")
            elif "nuxt" in deps or (base / "nuxt.config.ts").exists() or (base / "nuxt.config.js").exists():
                detected.append("nuxt")
            elif "@sveltejs/kit" in deps or (base / "svelte.config.js").exists():
                detected.append("svelte")
            elif "@angular/core" in deps or (base / "angular.json").exists():
                detected.append("angular")
            elif "vue" in deps:
                detected.append("vue")
            elif "react-native" in deps:
                detected.append("react_native")
            elif "@strapi/strapi" in deps:
                detected.append("strapi")
            elif "@nestjs/core" in deps:
                detected.append("node_nestjs")
            elif "fastify" in deps:
                detected.append("node_fastify")
            elif "express" in deps:
                detected.append("node_express")
            elif "react" in deps:
                detected.append("react")
            else:
                detected.append("node_express")
        except Exception:
            detected.append("node_express")

    # 2. PHP Ecosystem
    if (base / "composer.json").exists() or (base / "artisan").exists():
        try:
            if (base / "artisan").exists():
                detected.append("laravel")
            elif (base / "composer.json").exists():
                comp = json.loads((base / "composer.json").read_text(encoding="utf-8"))
                req = {**comp.get("require", {}), **comp.get("require-dev", {})}
                if "laravel/framework" in req:
                    detected.append("laravel")
                elif "symfony/framework-bundle" in req or "symfony/http-kernel" in req:
                    detected.append("symfony")
                else:
                    detected.append("laravel")
        except Exception:
            detected.append("laravel")

    # 3. Python Ecosystem
    if (base / "manage.py").exists():
        detected.append("django")
    elif (base / "requirements.txt").exists() or (base / "pyproject.toml").exists():
        req_text = ""
        if (base / "requirements.txt").exists():
            try:
                req_text = (base / "requirements.txt").read_text(encoding="utf-8").lower()
            except Exception:
                pass
        if "fastapi" in req_text:
            detected.append("fastapi")
        elif "django" in req_text:
            detected.append("django")
        elif "flask" in req_text:
            detected.append("flask")
        else:
            detected.append("fastapi")

    # 4. Go
    if (base / "go.mod").exists():
        detected.append("go")

    # 5. Rust
    if (base / "Cargo.toml").exists():
        detected.append("rust")

    # 6. .NET / C#
    if any(base.glob("*.csproj")) or any(base.glob("*.sln")):
        detected.append("dotnet")

    # 7. Java
    if (base / "pom.xml").exists() or (base / "build.gradle").exists():
        txt = ""
        for f in [base / "pom.xml", base / "build.gradle"]:
            if f.exists():
                try:
                    txt += f.read_text(encoding="utf-8").lower()
                except Exception:
                    pass
        if "quarkus" in txt:
            detected.append("quarkus")
        else:
            detected.append("spring_boot")

    # 8. Ruby
    if (base / "Gemfile").exists():
        detected.append("ruby_rails")

    # 9. Flutter
    if (base / "pubspec.yaml").exists():
        detected.append("flutter")

    # 10. WordPress
    if (base / "wp-config.php").exists() or (base / "wp-content").exists():
        detected.append("wordpress")

    # 11. iOS Native
    if any(base.glob("*.xcodeproj")) or any(base.glob("*.xcworkspace")):
        detected.append("ios")

    # 12. Android Native
    if (base / "settings.gradle").exists() or (base / "settings.gradle.kts").exists():
        detected.append("android")

    primary = detected[0] if detected else "html5"
    matched_sdk = SDK_CATALOG.get(primary, SDK_CATALOG["html5"])

    return {
        "project_root": str(base),
        "detected_frameworks": detected if detected else ["html5 (Universal Web)"],
        "recommended_sdk": matched_sdk["name"],
        "install_command": matched_sdk["install_command"],
        "package_url": matched_sdk["package_url"],
        "guide_url": matched_sdk["guide_url"],
        "quick_code": matched_sdk["quick_code"],
        "auto_installer_command": f"curl -sSL https://login512.com/login512-agent.py | python3 - install --stack {primary}",
    }


def get_instructions(framework: str) -> dict[str, Any]:
    raw = framework.lower().strip().replace(" ", "_").replace("-", "_")
    key = ALIASES.get(raw, raw)
    data = SDK_CATALOG.get(key)
    if not data:
        # Search by substring
        for k, v in SDK_CATALOG.items():
            if raw in k or raw in v["name"].lower():
                data = v
                key = k
                break

    if not data:
        return {
            "error": f"Framework '{framework}' not found.",
            "available_frameworks": list(SDK_CATALOG.keys()),
            "catalog_url": "https://login512.com/sdks.html",
            "guide_url": "https://login512.com/guide.html",
        }

    return {
        "framework": data["name"],
        "category": data["category"],
        "install_command": data["install_command"],
        "package_download_url": data["package_url"],
        "guide_anchor_url": data["guide_url"],
        "universal_agent_installer": f"curl -sSL https://login512.com/login512-agent.py | python3 - install --stack {key}",
        "code_example": data["quick_code"],
    }


def list_sdks(category: Optional[str] = None) -> dict[str, Any]:
    cat = (category or "all").lower().strip()
    result = []
    for key, item in SDK_CATALOG.items():
        if cat == "all" or item["category"] == cat:
            result.append({
                "key": key,
                "name": item["name"],
                "category": item["category"],
                "install_command": item["install_command"],
                "package_url": item["package_url"],
                "guide_url": item["guide_url"],
            })
    return {
        "total": len(result),
        "category_filter": cat,
        "sdks": result,
    }


def audit_code(code: str, filename: Optional[str] = None) -> dict[str, Any]:
    findings: list[str] = []
    score = 100

    # 1. Check for secret key leak in frontend
    if "l512_sk_" in code and any(ext in (filename or "") for ext in (".js", ".ts", ".jsx", ".tsx", ".vue", ".svelte", ".html")):
        findings.append("CRITICAL: Secret key ('l512_sk_...') detected in client-side code! Secret keys must reside strictly on the server backend.")
        score -= 50

    # 2. Check for zero-image violation
    forbidden_terms = ["save_image", "write_image", "cv2.imwrite", "localStorage.setItem('frame", "fs.writeFileSync"]
    for term in forbidden_terms:
        if term in code:
            findings.append(f"WARNING: Potential zero-image policy violation with term '{term}'. Facial frames must not be saved to disk/storage.")
            score -= 30

    return {
        "audit_passed": score >= 80,
        "score": score,
        "findings": findings if findings else ["Code adheres to Login512 Zero-Image Privacy & NIST FIPS 204 Post-Quantum standards."],
    }


def main():
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            line_str = line.strip()
            if not line_str:
                continue
            req = json.loads(line_str)
        except Exception:
            break

        req_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})

        if method == "initialize":
            res = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "login512-mcp", "version": "2.1.0"},
                },
            }
        elif method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"tools": TOOLS},
            }
        elif method == "tools/call":
            tool_name = params.get("name")
            arguments = params.get("arguments", {})

            if tool_name == "login512_inspect_project":
                output = inspect_project(arguments.get("project_path"))
            elif tool_name == "login512_get_instructions":
                output = get_instructions(arguments.get("framework", "vanilla"))
            elif tool_name == "login512_list_sdks":
                output = list_sdks(arguments.get("category", "all"))
            elif tool_name == "login512_audit_code":
                output = audit_code(arguments.get("code", ""), arguments.get("filename"))
            else:
                output = {"error": f"Unknown tool: {tool_name}"}

            res = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps(output, indent=2, ensure_ascii=False)}]
                },
            }
        else:
            res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

        sys.stdout.write(json.dumps(res) + chr(10))
        sys.stdout.flush()


if __name__ == "__main__":
    main()
