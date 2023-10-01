# 📃 About
Online auctions is a FastAPI-based application that implements a platform for creating lots and bids for them, at the end of the lot, an email is sent to the winner.

You can view all project endpoints at: http://127.0.0.1:8000/docs
> The project was created as a test task.

# ❕ Peculiarities
* The application follows a layered architecture, each layer of the application is responsible for its own logic.
* When logging in, you need to enter your email in the username field, this is a peculiarity of the FastAPI-Users library.
* Sending email letters to the winners of the lot is implemented through scheduled celery tasks, the frequency is 1 minute.
* The project is completely covered by tests using pytest library.

# 💽 Installation

1. #### Clone or download the repository.
2. #### Rename .env.dist to .env and populate it with all "Mailing" section variables.
3. #### Run docker services: `docker-compose -f docker/local/docker-compose.yaml up -d`

# 🌄 Demonstration

### Lot creation:
![Postman_8DDcxOga3s](https://github.com/FCTL3314/Online-Auctions-Backend/assets/97694131/67abfea2-0f6e-4583-a085-832e06259f28)

### Adding a bid per lot: 
![Postman_cfQfSiIktX](https://github.com/FCTL3314/Online-Auctions-Backend/assets/97694131/fabf1e5c-521d-4649-80a3-9e3d78b1d75b)

### Lot detail:
![Postman_hnI1TpTddi](https://github.com/FCTL3314/Online-Auctions-Backend/assets/97694131/004ab571-4d35-4eb6-a236-5d4b0555ad62)
