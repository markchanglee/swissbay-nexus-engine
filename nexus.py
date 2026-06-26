import argparse
from dotenv import load_dotenv
from python.engine.config_loader import load_yaml
from python.engine.build_manager import build_target
from python.engine.status_report import print_status
from python.engine.doctor import run_doctor

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Swissbay Nexus Engine")
    sub = parser.add_subparsers(dest="command")

    build = sub.add_parser("build", help="Build a draft from a registered target")
    build.add_argument("target", help="Target name from context_registry.yaml")

    sub.add_parser("status", help="Show basic Nexus Engine status")
    sub.add_parser("doctor", help="Run a local health check")

    args = parser.parse_args()

    if args.command == "build":
        config = load_yaml("config/config.yaml")
        registry = load_yaml("config/context_registry.yaml")
        output = build_target(args.target, config, registry)
        print(f"Draft created: {output}")

    elif args.command == "status":
        print_status()

    elif args.command == "doctor":
        raise SystemExit(run_doctor())

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
