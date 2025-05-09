# Creating a Config
-------
## Criminal Code
Articles are added to the json file according to the template:
```json
"Article Number": {
        "text": "Article disposition",
        "wanted": "Search priority (1 to 10)",
        "punishment": "Description of punishment"
    }
```



## Administrative Code / Road Code
Articles are added to the json file according to the template:
```json
"Article Number": {
        "text": "Article disposition",
        "punishment": "Description of punishment"
    }
```



## Ten-Codes:
To change the information about ten-codes you will have to change the file **`gui/index.html`**

Information about ten codes is divided into 2 sections

To change this you will need to find the div with the id **`"tencodes"`**

## Jurisdiction:
To change the jurisdiction information, you will also have to change the index.html file.
- In the code, find the div with the id **`"urisdicia"`** and change the information in it
- If you need to change the image, go to the gui directory and replace the Jurisdiction.png file

## Stages of the use of force:
To change the information about the stages of force application, find the div with the id **`"sila"`** in the index.html file

## Detention process:
To change the detention information, find the div with the id **`"process"`** in the index.html file

## Grounds for release:
To change the information about the reason for exemption, find the div with the ID **`"yasvoboden"`** in the index.html file.

