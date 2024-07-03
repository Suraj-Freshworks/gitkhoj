# gitkhoj
Search keywords in multiple GitHub org and get output in a CSV file

## Running via GitHub actions
1. Click on Actions.
2. Choose gitkhoj under All Workflows.
3. Enter the keywords separated by a comma if there are multiple keywords, and initiate the process.
4. Download the report once the scan is finished.

## Running locally
### 1. Clone the repo. And navigate to the gitkhoj directory. 
```
git clone https://github.com/Suraj-Freshworks/gitkhoj.git
cd gitkhoj
```
### 2. Starting the search
```
python3 main.py -t <GH_TOKEN> -q keyword1,keyword2,keyword3
```

To generate a **<GH_TOKEN>**, go to **Settings** by clicking your profile icon on the top-left. Then, click on **Developer settings** choose "Token (classic)" under the "Personal Access Tokens" menu, add a note, select "repo" under scopes, and click "Generate token". After generating the token, **authorize** all the orgs the search needs to be done. 

