Example template to use Conda + Docker for reproducible, easy to deploy models.

Blog post goes into more detail - find it here:

https://binal.pub/2018/10/data-science-with-docker-and-conda/

#### How to Use This All

As an example - here's my normal development process. Using it I can get from development to production with little friction, knowing that my code will work as expected, and that it won't negatively affect other processes on the production server.

##### Developing and Packaging

1. Clone the template down. Update the `environment.yml` as needed with packages I know I'll need, and run `docker-compose build`. This will build the development image with all the packages I defined installed within it.
2. Create a `.env_dev` file with development environment variables
3. Run `docker-compose up` and navigate to JupyterLab, which will be running on [http://localhost:8888](http://localhost:8888). We can access it by entering in the token `local_dev`.
4. From there prototype and develop a model/process using Jupyter Notebooks, saving any notebooks I create along the way into `/notebooks` as a development diary. Any final artifacts/models I plan on using in production I save within `/code`.
5. Once I have a final version of my code, save it (and any models it relies on) into `/code`.
6. Update the `docker-compose.prod.yml` file's `command` section to point to the my scripts' name, and the `image` section to point to my docker registry (something like my_registry/my_project:0.1).
7. Run `docker-compose -f docker-compose.prod.yml build` - this builds the production version of the image, packaging everything in the `/code` and `/notebooks` directories directly onto the image.
8. Run `docker-compose -f docker-compose.prod.yml push` which pushes that packaged image into my organizations docker registry.

At this point I now have an image that contains all my code, models, and other artifacts I need, that's preinstalled with exact versions of the Python packages and dependencies I require. It's stored in a central location where I can easily pull it down onto other servers.
