import json

def main():
  
  output = {
      "TODAY": [
      '⚠️ Warning Number 1',
      '⚠️ Warning Number 2',
      ],
      "YESTERDAY": [
      '240+ users have subscribed to Newsletter #1',
      'The post Post Name was suspended by Nick Mark'
      ]
  }

  print(json.dumps(output))

if __name__ == '__main__':
  main()