#!/usr/bin/env node
// Instalador de la skill anti-slop-es. Sin dependencias.
import { cpSync, existsSync, mkdirSync, rmSync } from "node:fs";
import { homedir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const RAIZ = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const NOMBRE = "anti-slop-es";
const args = process.argv.slice(2);
const flag = (...n) => n.some((x) => args.includes(x));

if (flag("-h", "--help", "--ayuda")) {
  console.log(`
  npx ${NOMBRE}                instala en ~/.claude/skills/${NOMBRE}
  npx ${NOMBRE} --proyecto     instala en ./.claude/skills/${NOMBRE}
  npx ${NOMBRE} --dir <ruta>   instala en <ruta>/${NOMBRE}
  npx ${NOMBRE} --desinstalar  borra la skill del destino
`);
  process.exit(0);
}

const i = args.findIndex((a) => a === "--dir");
const base = i !== -1 && args[i + 1]
  ? resolve(args[i + 1])
  : flag("--proyecto", "--project")
    ? resolve(process.cwd(), ".claude/skills")
    : join(homedir(), ".claude", "skills");

const destino = join(base, NOMBRE);

if (flag("--desinstalar", "--uninstall")) {
  if (!existsSync(destino)) {
    console.log(`No hay nada en ${destino}`);
    process.exit(0);
  }
  rmSync(destino, { recursive: true, force: true });
  console.log(`Borrado ${destino}`);
  process.exit(0);
}

mkdirSync(destino, { recursive: true });
for (const item of ["SKILL.md", "references", "scripts"]) {
  cpSync(join(RAIZ, item), join(destino, item), { recursive: true });
}

console.log(`
  anti-slop-es instalada en ${destino}

  Reinicia Claude Code y pídele:  "revisa este texto con anti-slop-es"
  O corre el detector directo:    python3 ${join(destino, "scripts", "detectar_slop.py")} archivo.md --verbose
`);
