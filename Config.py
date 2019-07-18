import psycopg2
from winterboot.Service import Service
import sys
from os.path import dirname

@Service
class Config(object):
    #input
    TRAINING_SET_FILE = '/tmp/train_set.csv'
    PROBLEM_SET_FILE = '/tmp/production_set.csv'

    #database
    DATABASE_CONNECTOR = psycopg2
    CONNECTION_STRING = "postgresql://guest:s3cr3t@jobe.kodekonveyor.com/transactions"
    SQL_TO_OBTAIN_CATEGORIES = "select id, category from categories"
    SQL_TO_OBTAIN_TRANSACTION_BY_OID = "select * from transactions where oid={0}"
    SQL_TO_UPDATE_RECORD = "update {0.table} set category='{0.choice[1]}' where oid={0.oid}"

    #neural net parameters
    FIRST_LAYER_NEURONS=50
    SECOND_LAYER_NEURONS=30
    BATCH_SIZE=50
    EPOCHS=80
    MIN_PROBABILITY=0.1
    MIN_ACCURACY=0.7

    ID_COLUMN_POSITION_IN_CATEGORIES_TABLE = 0
    TRAINING_SET_ID_COLUMN = "id"
    TRAINING_SET_INPUT_COLUMN = "comment"
    TRAINING_SET_OUTPUT_COLUMN = "category"
    TRAINING_SET_COLUMNS = [TRAINING_SET_ID_COLUMN, TRAINING_SET_INPUT_COLUMN, TRAINING_SET_OUTPUT_COLUMN]
    
    PROBLEM_SET_ID_COLUMN = "id"
    PROBLEM_SET_INPUT_COLUMN = "comment"
    PROBLEM_SET_COLUMNS = [PROBLEM_SET_ID_COLUMN, PROBLEM_SET_INPUT_COLUMN]
    CHOICE_FORMAT_REGEX = "\S+"
    OPTION_DISPLAY_FORMAT = "\t {0}: {1} {2}"

    def figureOutTable(self, row):
        return "transactions"
