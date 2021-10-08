# imports 
import os
import sys
from pathlib import Path
from numpy import ndarray
# set paths
vue_dir = sys.argv[1]
vue_views = '/src/views'
vue_router = '/src/router'
# globals
fileNames = []

def updateRouter():
    global fileNames 
    # same process but first check to see if elemnts already exist
    #indexFile = open(vue_dir + '' + vue_router + '\\index.js','w')
    #indexFile.truncate(0)
    createRouter()

def createRouter():
    global fileNames
    # create index.js based on the /views folder
    for base, dirs, files in os.walk(vue_dir + '' + vue_views):
        fileNames.extend(files) 
    writeTo(fileNames)

def writeTo(fileNames): 
    with open(vue_dir + '' + vue_router + '\\index.js', 'w') as fp:
        print('Adding createRouter from vue-router...')
        print('Adding createWebHistory from vue-router...')
        fp.write("import { createRouter, createWebHistory } from 'vue-router';\n")

        # routes = [] -> create and insert into index.js
        routes = ['']*len(fileNames)
        imports = ['']*len(fileNames)
        index = 0
        for name in fileNames:
            editName = Path(name).stem
            routes[index] = "  { path: '" + editName + "', name: '" + editName + "', component: '" + editName + "' },"
            imports[index] = "import " + editName + " from '" + vue_views + "/" + editName + "';"
            index += 1
              
        router = "const router = createRouter({\nhistory: createWebHistory(process.env.BASE_URL),\nroutes\n});\n\nexport default router;\n"
        # add imports 
        print('Writing the imports...')
        for x in imports:
            fp.write(x + "\n")
        # add routes []
        print('Writing the routes...')
        fp.write("\n\nconst routes = [\n")
        for y in routes:
            fp.write(y + "\n")
        fp.write("];")
        # add the router component
        print('Adding router component...')
        fp.write("\n\n" + router)

def main():        
    # check if folders exist
    if os.path.isdir(vue_dir):
        if os.path.isdir(vue_dir + '' + vue_views):
            if os.path.isdir(vue_dir + '' + vue_router):
                updateRouter()
            else:
                os.makedirs(vue_dir + '' + vue_router)
                createRouter()        
        else:
            os.makedirs(vue_dir + '' + vue_views)
    else:
        print('ERROR: please use a vaild vue path')

main()