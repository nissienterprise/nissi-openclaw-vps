#!/usr/bin/env python3
"""Upload OpenClaw documentation to Confluence space 'Nissi Automate AI' (NAA)."""

import os
import json
import base64
import urllib.request
import urllib.error
import markdown
from pathlib import Path

# --- Config ---
JIRA_EMAIL = "mrodriguez@nissienterprise.com"
JIRA_TOKEN = "ATATT3xFfGF0fabniyfUHi5MJUCiWUMd59W7Srnq0_kqDfbiMb9SooSyakPfYxiiUNCMi9iqKXEPZfy1GuSTyPAYOyIEJDDrnNSj0e1lAFBzsviq9neaV1RjKumWDkOhKxNqHxLCyFI6l4HiPhAsQqPrsu28lQBNk_LTBMLLK7ShC3Zu-9scSVk=0F99BFE3"
BASE_URL = "https://nissitechnology.atlassian.net/wiki"
SPACE_KEY = "NAA"
PROJECT_ROOT = Path("/Users/mrodriguez/projects/openclaw")

AUTH = base64.b64encode(f"{JIRA_EMAIL}:{JIRA_TOKEN}".encode()).decode()
HEADERS = {
    "Authorization": f"Basic {AUTH}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}

def api_request(method, path, data=None):
    url = f"{BASE_URL}/rest/api{path}"
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        err = e.read().decode()
        print(f"  ERROR {e.code} on {method} {path}: {err[:300]}")
        return None

def md_to_storage(md_text):
    """Convert markdown to Confluence storage format (HTML-based)."""
    html = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "toc", "nl2br"]
    )
    return html

def get_page_by_title(title, space_key=SPACE_KEY):
    result = api_request("GET", f"/content?type=page&spaceKey={space_key}&title={urllib.parse.quote(title)}&expand=version")
    if result and result.get("results"):
        return result["results"][0]
    return None

def create_or_update_page(title, body_html, parent_id=None, space_key=SPACE_KEY):
    existing = get_page_by_title(title, space_key)

    if existing:
        page_id = existing["id"]
        version = existing["version"]["number"] + 1
        print(f"  Updating: '{title}' (id={page_id})")
        data = {
            "id": page_id,
            "type": "page",
            "title": title,
            "version": {"number": version},
            "body": {
                "storage": {
                    "value": body_html,
                    "representation": "storage"
                }
            }
        }
        result = api_request("PUT", f"/content/{page_id}", data)
        return result["id"] if result else None
    else:
        print(f"  Creating: '{title}'")
        data = {
            "type": "page",
            "title": title,
            "space": {"key": space_key},
            "body": {
                "storage": {
                    "value": body_html,
                    "representation": "storage"
                }
            }
        }
        if parent_id:
            data["ancestors"] = [{"id": parent_id}]
        result = api_request("POST", "/content", data)
        return result["id"] if result else None

def read_md(path):
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        return f"# Error reading file\n{e}"

def folder_display_name(folder_name):
    """Convert folder slug to readable title."""
    names = {
        "01-empresa": "01 - Empresa",
        "02-infraestructura": "02 - Infraestructura",
        "03-agentes": "03 - Agentes",
        "04-flujos": "04 - Flujos",
        "05-stack-tecnologico": "05 - Stack Tecnológico",
        "06-roadmap": "06 - Roadmap",
        "07-prompts": "07 - Prompts",
        "08-kpis": "08 - KPIs",
        "09-presupuesto": "09 - Presupuesto",
        "10-ambientes": "10 - Ambientes",
        "11-logging": "11 - Logging",
        "wing-administrativa": "Wing Administrativa",
        "wing-software": "Wing Software",
        "flujos-especializados": "Flujos Especializados",
        "blog-automation": "Blog Automation",
        "lead-management": "Lead Management",
        "workspace": "Workspace / Sistema",
        "documentacion": "Documentación",
    }
    return names.get(folder_name, folder_name.replace("-", " ").title())

def file_display_name(filename):
    """Convert filename to readable title."""
    name = filename.stem
    titles = {
        "README": "README - Índice",
        "mision-vision-valores": "Misión, Visión y Valores",
        "servicios": "Servicios",
        "seguridad": "Seguridad",
        "vps-setup": "Configuración VPS",
        "nte-main": "NTE Main (Agente Principal)",
        "nte-cx": "NTE-CX (Customer Experience)",
        "nte-content": "NTE-Content (Contenido)",
        "nte-analytics": "NTE-Analytics",
        "nte-pm": "NTE-PM (Project Manager)",
        "nte-security": "NTE-Security",
        "nte-backend": "NTE-Backend",
        "nte-frontend": "NTE-Frontend",
        "nte-mobile": "NTE-Mobile",
        "nte-data": "NTE-Data",
        "nte-qa": "NTE-QA",
        "nte-devops": "NTE-DevOps",
        "nte-docs": "NTE-Docs",
        "nte-trend-scout": "NTE-Trend Scout",
        "nte-copywriter": "NTE-Copywriter",
        "nte-publisher": "NTE-Publisher",
        "nte-propagator": "NTE-Propagator",
        "nte-lead-intake": "NTE-Lead Intake",
        "nte-lead-nurture": "NTE-Lead Nurture",
        "jarvis": "Jarvis",
        "flujo-desarrollo-software": "Flujo - Desarrollo de Software",
        "flujo-leads": "Flujo - Leads",
        "flujo-blog-semanal": "Flujo - Blog Semanal",
        "flujo-customer-service": "Flujo - Customer Service",
        "herramientas": "Herramientas del Stack",
        "implementacion-2026": "Roadmap - Implementación 2026",
        "prompts-por-agente": "Prompts por Agente",
        "nte-main-system-prompt": "NTE Main - System Prompt",
        "metricas-exito": "KPIs - Métricas de Éxito",
        "costos-estimados": "Presupuesto - Costos Estimados",
        "ambientes": "Ambientes",
        "02-nte-logger": "NTE Logger",
        "03-infraestructura": "Infraestructura de Logging",
        "04-grafana": "Grafana",
        "IDENTITY": "Identidad del Sistema",
        "BOOTSTRAP": "Bootstrap",
        "TOOLS": "Herramientas",
        "SOUL": "Soul - Principios",
        "USER": "Usuario",
        "HEARTBEAT": "Heartbeat",
        "AGENTS": "Agentes del Sistema",
    }
    return titles.get(name, name.replace("-", " ").replace("_", " ").title())

import urllib.parse

def main():
    # Get space homepage
    space_info = api_request("GET", f"/space/{SPACE_KEY}?expand=homepage")
    if not space_info:
        print("ERROR: Cannot access space NAA")
        return

    homepage_id = space_info["homepage"]["id"]
    print(f"Space homepage ID: {homepage_id}")

    # === ROOT: Documentación ===
    print("\n[1/2] Creating root 'Documentación OpenClaw'...")
    root_html = md_to_storage(read_md(PROJECT_ROOT / "README.md"))
    root_id = create_or_update_page("Documentación OpenClaw", root_html, parent_id=homepage_id)
    if not root_id:
        print("ERROR: Could not create root page")
        return
    print(f"  Root page ID: {root_id}")

    # === WORKSPACE ===
    print("\n[2/2] Creating Workspace pages...")
    workspace_dir = PROJECT_ROOT / "workspace"
    workspace_id = create_or_update_page(
        "Workspace / Sistema",
        "<p>Documentación interna del sistema de agentes OpenClaw.</p>",
        parent_id=root_id
    )
    if workspace_id:
        for md_file in sorted(workspace_dir.glob("*.md")):
            title = file_display_name(md_file)
            html = md_to_storage(read_md(md_file))
            create_or_update_page(title, html, parent_id=workspace_id)

    # === DOCUMENTACION FOLDER ===
    doc_dir = PROJECT_ROOT / "documentacion"

    # Create top-level documentacion page
    doc_readme = doc_dir / "README.md"
    doc_root_html = md_to_storage(read_md(doc_readme)) if doc_readme.exists() else "<p>Documentación del proyecto.</p>"
    doc_root_id = create_or_update_page("Documentación", doc_root_html, parent_id=root_id)
    if not doc_root_id:
        print("ERROR: Could not create Documentación page")
        return

    # Ordered sections
    sections = [
        "01-empresa",
        "02-infraestructura",
        "03-agentes",
        "04-flujos",
        "05-stack-tecnologico",
        "06-roadmap",
        "07-prompts",
        "08-kpis",
        "09-presupuesto",
        "10-ambientes",
        "11-logging",
    ]

    for section in sections:
        section_dir = doc_dir / section
        if not section_dir.exists():
            continue

        section_name = folder_display_name(section)
        print(f"\n--- Section: {section_name} ---")

        # Section readme or placeholder
        section_readme = section_dir / "README.md"
        section_html = md_to_storage(read_md(section_readme)) if section_readme.exists() else f"<p>Sección: {section_name}</p>"
        section_id = create_or_update_page(section_name, section_html, parent_id=doc_root_id)
        if not section_id:
            continue

        # Process files and subdirectories
        process_directory(section_dir, section_id, skip_readme=True)

    print("\n✓ Upload complete!")

def process_directory(directory, parent_id, skip_readme=False):
    """Recursively process a directory, creating pages for files and subdirs."""
    # First handle markdown files directly in this dir
    for md_file in sorted(directory.glob("*.md")):
        if skip_readme and md_file.name == "README.md":
            continue
        title = file_display_name(md_file)
        html = md_to_storage(read_md(md_file))
        create_or_update_page(title, html, parent_id=parent_id)

    # Then handle subdirectories
    for subdir in sorted([d for d in directory.iterdir() if d.is_dir()]):
        subdir_name = folder_display_name(subdir.name)
        print(f"  Subfolder: {subdir_name}")

        readme = subdir / "README.md"
        sub_html = md_to_storage(read_md(readme)) if readme.exists() else f"<p>{subdir_name}</p>"
        sub_id = create_or_update_page(subdir_name, sub_html, parent_id=parent_id)
        if sub_id:
            process_directory(subdir, sub_id, skip_readme=True)

if __name__ == "__main__":
    main()
