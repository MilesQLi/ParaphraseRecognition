@echo 'start build'

::make -f Makefile.win build
javac -encoding UTF-8 -classpath "stanford-parser.jar;stanford-parser-3.4.1-models.jar;." DependencyAnalysis.java

java -classpath "stanford-parser.jar;stanford-parser-3.4.1-models.jar;."  DependencyAnalysis ./data/train_data.txt ./data/train_data_dependency.txt ./data/dev_data.txt ./data/dev_data_dependency.txt ./data/test_data.txt ./data/test_data_dependency.txt 

python main.py train_data.txt train_data_dependency.txt dev_data.txt dev_data_dependency.txt dev_gold.txt test_data.txt test_data_dependency.txt test_gold.txt
