echo 'start build'

make build

java -classpath "stanford-parser.jar:stanford-parser-3.4.1-models.jar:." DependencyAnalysis ./data/train_data.txt ./data/train_data_dependency.txt ./data/dev_data.txt ./data/dev_data_dependency.txt ./data/test_data.txt ./data/test_data_dependency.txt 

python main.py ./data/train_data.txt ./data/train_data_dependency.txt ./data/dev_data.txt ./data/dev_data_dependency.txt ./data/dev_gold.txt ./data/test_data.txt ./data/test_data_dependency.txt ./data/test_gold.txt