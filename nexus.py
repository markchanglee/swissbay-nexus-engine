import argparse
from dotenv import load_dotenv
from python.engine.config_loader import load_yaml
from python.engine.build_manager import build_target
from python.engine.status_report import print_status
from python.engine.doctor import run_doctor
from python.engine.registry import run_registry
from python.engine.roadmap import run_roadmap
from python.engine.validate_command import run_validate
from python.engine.review import run_review
from python.engine.object_builder import run_create

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Swissbay Nexus Engine")
    sub = parser.add_subparsers(dest="command")

    build = sub.add_parser("build", help="Build a draft from a registered target")
    build.add_argument("target", help="Target name from context_registry.yaml")

    create = sub.add_parser("create", help="Create a Nexus object file from registry metadata")
    create.add_argument("target", help="Business object key from config/registry.yaml")

    review = sub.add_parser("review", help="Review a draft against Nexus standards")
    review.add_argument("target", help="Target name to review")

    validate = sub.add_parser("validate", help="Validate Markdown files against Nexus standards")
    validate.add_argument(
        "--path",
        action="append",
        dest="paths",
        help="Optional path to scan. Can be used more than once."
    )

    sub.add_parser("status", help="Show basic Nexus Engine status")
    sub.add_parser("doctor", help="Run a local health check")
    sub.add_parser("registry", help="Show the Nexus registry")
    sub.add_parser("roadmap", help="Show the Nexus roadmap")

    args = parser.parse_args()

    if args.command == "build":
        config = load_yaml("config/config.yaml")
        registry = load_yaml("config/context_registry.yaml")
        output = build_target(args.target, config, registry)
        print(f"Draft created: {output}")

    elif args.command == "create":
        raise SystemExit(run_create(args.target))

    elif args.command == "review":
        raise SystemExit(run_review(args.target))

    elif args.command == "status":
        print_status()

    elif args.command == "doctor":
        raise SystemExit(run_doctor())

    elif args.command == "registry":
        raise SystemExit(run_registry())

    elif args.command == "roadmap":
        raise SystemExit(run_roadmap())

    elif args.command == "validate":
        raise SystemExit(run_validate(scan_paths=args.paths))

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
