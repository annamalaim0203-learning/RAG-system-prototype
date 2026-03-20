import argparse
from ingest import ingest_pdf
from generate import answer_question

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    p_ingest = sub.add_parser("ingest")
    p_ingest.add_argument("--pdf", required=True, help="Path to PDF")

    p_ask = sub.add_parser("ask")
    p_ask.add_argument("--q", required=True, help="Question")

    args = parser.parse_args()

    if args.command == "ingest":
        ingest_pdf(args.pdf)
    elif args.command == "ask":
        answer_question(args.q)

if __name__ == "__main__":
    main()
