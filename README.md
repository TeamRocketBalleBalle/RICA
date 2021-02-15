# RICA

> Remote Intensive Care App

---

This Repo will be used by some "_ultra pro max lite_" minecraft players to build our 1st semester group project :sunglasses: :fire::fire: hello 1234

---

## How to Run:

### 2 ways to run the app:
  1) Using `flask run` **[DEVELOPMENT SERVER ONLY]**
      - open the ![Back_End](Back_End) directory in terminal
      - run `flask run`
  
  2) Manually from python **[DEVELOPMENT SERVER ONLY]**
      - again, in ![Back_End](Back_End) directory, run `python -m __init__` or `python -m app`
      - Alternatively, you can run them from the repo's root directory, by opening the terminal in [RICA](RICA) \
      and executing `python -m Back_End.app` or `python -m Back_End.__init__`

### [To run a production server](https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/#run-with-a-production-server)

  - Open terminal in repository root
  - Run the following: `waitress-serve --call "Back_End:create_app"`
  - A production server will start automatically now
