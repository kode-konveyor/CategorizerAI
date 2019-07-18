import psycopg2
from winterboot.Service import Service
import sys
from os.path import dirname

@Service
class Config(object):
    DATABASE_CONNECTOR = psycopg2
    CONNECTION_STRING = "postgresql://username:s3cr3t@example.com:5432/transactions"
    SQL_TO_OBTAIN_CATEGORIES = "SELECT id,category1,category2 from categories"
    SQL_TO_OBTAIN_TRANSACTION_BY_OID = "select * from all_transactions where oid={0}"
    SQL_TO_UPDATE_RECORD = "update {0.table} set category1='{0.choice[1]}', category2='{0.choice[2]}' where oid={0.oid}"

    FIRST_LAYER_NEURONS=11
    SECOND_LAYER_NEURONS=22
    BATCH_SIZE=33
    EPOCHS=44
    MIN_PROBABILITY=0.1
    MIN_ACCURACY=0.7
    ID_COLUMN_POSITION_IN_CATEGORIES_TABLE = 0
    dirName = dirname(sys.modules[__name__].__file__)
    TRAINING_SET_FILE = dirName+'/train_set.csv'
    PROBLEM_SET_FILE = dirName+'/problem_set.csv'
    TRAINING_SET_ID_COLUMN = "id"
    TRAINING_SET_INPUT_COLUMN = "comment"
    TRAINING_SET_OUTPUT_COLUMN = "category"
    TRAINING_SET_COLUMNS = [TRAINING_SET_ID_COLUMN, TRAINING_SET_INPUT_COLUMN, TRAINING_SET_OUTPUT_COLUMN]
    
    PROBLEM_SET_ID_COLUMN = "id"
    PROBLEM_SET_INPUT_COLUMN = "comment"
    PROBLEM_SET_COLUMNS = [PROBLEM_SET_ID_COLUMN, PROBLEM_SET_INPUT_COLUMN]
    CHOICE_FORMAT_REGEX = "\S+,\S+"
    OPTION_DISPLAY_FORMAT = "\t {0}: {1} {2}"

    def figureOutTable(self, row):
        return "transactions"
