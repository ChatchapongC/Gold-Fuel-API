Gold-Fuel Relationship
===========================================

There are many factors that affect the gold price. Fuel price is one of the factors of  that will change in the same way with the gold price. This API that can get the gold price and fuel price to compare together. Also can view the specific detail of gold price or fuel price such as average price per month, highest price of gold, amount of flow of fuel price, etc. 
(The data of both fuel and gold is from January to November in 2020 )

# Author
**Chatchapong Chumapda 6010546877**   
_Department of Computer Engineering,            
Software and Knowledge Engineering,   
Kasetsart University_

# Prerequisities
- **Python** (v.3.6 or newer) : [Download](https://www.python.org/downloads/)

- **Virtual Environment**
    ```shell script
    > pip install virtualenv
    ```      
- **openapi-generator-cli-4.3.1.jar** - [Download](https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/4.3.1/openapi-generator-cli-4.3.1.jar) and put in `Gold-Fuel-API` folder

# Installing 
1. Clone the project from [Gold-Fuel-API](https://github.com/ChatchapongC/Gold-Fuel-API) on **Terminal**.
    ```shell script
    # Clone with HTTPS
    > git clone https://github.com/ChatchapongC/Gold-Fuel-API.git
   
    # Clone with SSH
    > git clone git@github.com:ChatchapongC/Gold-Fuel-API.git
    ``` 
2. Change your current working directory into folder `Gold-Fuel-API` and create a new virtual environment.
    ```shell script
    > cd Gold-Fuel-API/
    > virtualenv env
    ```
3. Activate the virtual environment.
    ```shell script
    # For MacOS
    > source ./env/bin/activate

    # For Windows
    > .\env\Scripts\activate
    ```
4. Install dependencies from file `requirements.txt`.
    ```shell script
    (env) > pip install -r requirements.txt
   
    # to exit virualenv
    (env) > deactivate
    ```
5. Change a file name `config.py.example` into `config.py.`.
     ```shell script
    # For windows
    (env) > rename config.py.example config.py
     
    # For MacOS
    (env) > mv config.py.example config.py
    ```
# Run Application
1. Generate code from the OAS.
    ```shell script
    (env) > java -jar openapi-generator-cli-4.3.1.jar generate -i openapi/gold-fuel-api.yaml -o autogen -g python-flask
    ```
2. Start the REST API server.
    ```shell script
    (env) > python app.py
    ```
3. In another terminal, run openapi-to-graphql with CORS
(Cross-Origin Resource Sharing) enabled
     ```shell script
    (env) > openapi-to-graphql --cors -u http://localhost:8080/gold-fuel openapi/gold-fuel-api.yaml
    ```

4. Then go to : [localhost:8000/gold-fuel/ui](http://localhost:8000/gold-fuel/ui) to visit API on Swagger.