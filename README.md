#Install

pip3 install CategorizerAI

#Usage, Example

There is an example database using a dataset with US government transactions.
The Config.py in the source root is a configuration to use it.
The updater script in the same location drives data acquisition and updating.

You can set up your own setup by studying the example

The hardest part is tuning the AI for the particular data you have.
use FIRST_LAYER_NEURONS, SECOND_LAYER_NEURONS, BATCH_SIZE and EPOCHS in Config.py
for the tuning. Bigger is not always better!

It might happen that the neural net cannot learn the data with enough accuracy.
In this case it tells you so, and exits.

#DEPENDENCIES

    apt install python3-pip libpq-dev
    pip3 install pandas tensorflow keras psycopg2 

