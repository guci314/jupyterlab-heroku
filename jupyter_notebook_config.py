# https://devcenter.heroku.com/articles/ssl-endpoint
#
# As long as the notebook lives in the herokuapp.com domain,
# we have SSL certificates enabled for encryption purposes.
c.NotebookApp.ip = "*"
c.NotebookApp.open_browser = False
c.NotebookApp.password="sha1:9eba103a32e3:ae0761f75b406ff8f385422e0e9886b9e7bbf2ca"
c.NotebookApp.token=""
