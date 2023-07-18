import base64
import json

def main():
  
  output = {
      "TODAY": [
      "⚠️ Warning Number 1",
      "⚠️ Warning Number 2",
      ],
      "YESTERDAY": [
      "240+ users have subscribed to Newsletter #1",
      "The post Post Name was suspended by Nick Mark"
      ]
  }
  output_json = json.dumps(output)
  output_bytes = output_json.encode("utf-8")
  output_encoded = base64.b64encode(output_bytes)
  print(output_encoded.decode("utf-8"))

if __name__ == '__main__':
  main()