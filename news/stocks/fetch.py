import argparse
import base64
import finviz
import json

def parse_args():
    parser = argparse.ArgumentParser(description="Get news article via the Unofficial API for finviz.com")
    parser.add_argument('--symbols','-s', help="Specify the stock symbol(s) to search for, e.g. 'TSLA,AMZN,AAPL'", required=True)
    parser.add_argument('--limit','-l', required=False, default=25)
    parser.add_argument('--start','-sd', help='Not yet implemented', required=False)
    parser.add_argument('--end','-ed', help='Not yet implemented', required=False)
    parser.add_argument('--verbose','-v', action='store_true', required=False, default=False)
    return parser.parse_known_args()

def main():

  # CLI Args
  args, unknown= parse_args()

  symbols = args.symbols.split(',')

  articles = []
  output = {}
  limit = int(args.limit)

  for symbol in symbols:
    symbol_u = symbol.upper()
    symbol_articles = finviz.get_news(symbol_u)[0:limit]
    output[f"Here are {limit} articles for {symbol_u}"] = symbol_articles
  print(output)
  quit()
  output_json = json.dumps(output)
  output_bytes = output_json.encode("utf-8")
  output_encoded = base64.b64encode(output_bytes)
  print(output_encoded.decode("utf-8"))

if __name__ == '__main__':
  main()