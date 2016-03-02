ENTRY_POINT = DependencyAnalysis.java

CLASS_PATH = "stanford-parser.jar:stanford-parser-3.4.1-models.jar:." 

SOURCE_FILES = \
DependencyAnalysis.java

JAVAC = javac

JFLAGS = -encoding UTF-8

all:build

build: 
	$(JAVAC) $(JFLAGS) -classpath $(CLASS_PATH) $(ENTRY_POINT)

clean:
	$(RM) *.class
