运行顺序prerun.sh  ->  run.sh

本项目依赖斯坦福句法分析工具，包括stanford-parser.jar和stanford-parser-3.4.1-models.jar。还依赖一系列python开发库包括nltk、scikit-learn、numpy、matplotlib、scipy,并需要nltk下的资料库。可通过prerun.sh脚本自动下载此系列库文件。scikit-learn通过脚本下载可能会失败，如果失败还需到http://www.lfd.uci.edu/~gohlke/pythonlibs/#scikit-learn下载。辛苦啦~

运行时需要先运行DependencyAnalysis.class java程序获取依赖关系文件，再运行main.py进行主程序运行。可通过run.sh脚本文件完成。

main.py主程序入口。通过训练集、开发集训练和交叉验证对模型超参数寻优，并在测试集上测试。

main_dev.py为开发本项目时的主程序入口，通过训练集训练模型并交叉验证超参数寻优，在开发集上测试模型性能。