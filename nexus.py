import argparse
from dotenv import load_dotenv
from python.engine.config_loader import load_yaml
from python.engine.build_manager import build_target
from python.engine.status_report import print_status

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Swissbay Nexus Engine")
    sub = parser.add_subparsers(dest="command")

    build = sub.add_parser("build")
    build.add_argument("target", help="Target name from context_registry.yaml")

    sub.add_parser("status")

    args = parser.parse_args()

    if args.command == "build":
        config = load_yaml("config/config.yaml")
        registry = load_yaml("config/context_registry.yaml")
        output = build_target(args.target, config, registry)
        print(f"Draft created: {output}")

    elif args.command == "status":
        print_status()

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
