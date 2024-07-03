# gitkhoj
Search keywords in multiple github orgs and get output in CSV file

## Running via GitHub actions
1. Click on Actions.
2. Choose gitkhoj under All Workflows.
3. Input the keywords separated by a comma if there are multiple. Start the flow. 
4. Download the report once the scan is complete.

## Running locally
### 1. Clone the repo. And cd to gitkhoj. 
```
git clone https://github.com/Suraj-Freshworks/gitkhoj.git
cd gitkhoj
```
### 2. Starting the search
```
python3 main.py -t <GH_TOKEN> -q keyword1,keyword2,keyword3
```

For generating **<GH_TOKEN>**, click on the **Settings** by clicking your profile icon on the top-left. Click on **Developer settings** and select Token (classic) under the Personal Access Tokens menu. Add a note and check **repo** under scopes. Click on Generate token. 


