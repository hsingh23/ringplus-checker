**This is a Ringplus website watcher app that texts you when the free plans on the website changes.**

**How to use with docker:**  
1. Edit site-checker/config.json - use the example_config.json as a template  
2. docker build -t SITENAME .
3. docker run -d SITENAME  

To stop (and remove): docker rm -f SITENAME
To see if checker is running: docker ps
