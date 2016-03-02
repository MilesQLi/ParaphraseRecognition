/*

author:Li Qi
mail:stormier@126.com


*/


import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.StringReader;

import edu.stanford.nlp.process.Tokenizer;
import edu.stanford.nlp.process.TokenizerFactory;
import edu.stanford.nlp.process.CoreLabelTokenFactory;
import edu.stanford.nlp.process.DocumentPreprocessor;
import edu.stanford.nlp.process.PTBTokenizer;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.ling.CoreLabel.OutputFormat;
import edu.stanford.nlp.ling.HasWord;
import edu.stanford.nlp.ling.Sentence;
import edu.stanford.nlp.trees.*;
import edu.stanford.nlp.parser.lexparser.LexicalizedParser;

public class DependencyAnalysis {

	private static LexicalizedParser lp;
	private static TreebankLanguagePack tlp;
	private static GrammaticalStructureFactory gsf;
	private static TokenizerFactory<CoreLabel> tokenizerFactory;

	public static void main(String[] args) {
		lp = LexicalizedParser
				.loadModel("edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz");
		tlp = new PennTreebankLanguagePack();
		gsf = tlp.grammaticalStructureFactory();
		tokenizerFactory = PTBTokenizer
				.factory(new CoreLabelTokenFactory(), "");

		if (args.length == 1) {
			if (args[0].equals("train")) {
				parse_train_file("train_data.txt", "train_data_dependency.txt");
			} else if (args[0].equals("dev")) {
				parse_dev_or_test_file("dev_data.txt", "dev_data_dependency.txt");
			} else if (args[0].equals("test")) {
				parse_dev_or_test_file("test_data.txt", "test_data_dependency.txt");
			}
		} else if (args.length == 6) {
			parse_train_file(args[0], args[1]);
			parse_dev_or_test_file(args[2], args[3]);
			parse_dev_or_test_file(args[4], args[5]);
		} else {
			parse_train_file("train_data.txt", "train_data_dependency.txt");
			parse_dev_or_test_file("dev_data.txt", "dev_data_dependency.txt");
			parse_dev_or_test_file("test_data.txt", "test_data_dependency.txt");
		}
	}
	
// get dependency relation of train data 
	public static void parse_train_file(String input, String output) {
		File input_file = new File(input);
		if (!input_file.exists() || !input_file.isFile()) {
			return;
		}
		OutputStreamWriter writer;
		try {
			writer = new OutputStreamWriter(new FileOutputStream(output),"UTF-8");

			try {
				FileInputStream fileInputStream = new FileInputStream(
						input_file);
				InputStreamReader inputStreamReader = new InputStreamReader(
						fileInputStream, "UTF-8");
				BufferedReader reader = new BufferedReader(inputStreamReader);

				String line = "";
				int i = 1;
				while ((line = reader.readLine()) != null) {
					String[] content = line.split("\t");
					writer.write(content[1] + '\t' + content[2] + '\t');
					for (TypedDependency dependency:dependency_parse(content[3]))
					{
						writer.write(dependency.toString(OutputFormat.VALUE)+' ');
					}
					writer.write('\t');
					for (TypedDependency dependency:dependency_parse(content[4]))
					{
						writer.write(dependency.toString(OutputFormat.VALUE)+' ');
					}					
					writer.write('\n');
					writer.flush();
					System.out.println(i++);
				}

				fileInputStream.close();
				inputStreamReader.close();
				reader.close();

				writer.close();

			} catch (Exception e) {
				e.printStackTrace();
			}
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
	}

	
// get dependency relation of dev data or test data 
	public static void parse_dev_or_test_file(String input, String output) {
		File input_file = new File(input);
		if (!input_file.exists() || !input_file.isFile()) {
			return;
		}
		OutputStreamWriter writer;
		try {
			writer = new OutputStreamWriter(new FileOutputStream(output),"UTF-8");

			try {
				FileInputStream fileInputStream = new FileInputStream(
						input_file);
				InputStreamReader inputStreamReader = new InputStreamReader(
						fileInputStream, "UTF-8");
				BufferedReader reader = new BufferedReader(inputStreamReader);

				String line = "";
				int i = 1;
				while ((line = reader.readLine()) != null) {
					String[] content = line.split("\t");
					writer.write(content[0] + '\t' + content[1] + '\t');
					for (TypedDependency dependency:dependency_parse(content[2]))
					{
						writer.write(dependency.toString(OutputFormat.VALUE)+' ');
					}
					writer.write('\t');
					for (TypedDependency dependency:dependency_parse(content[3]))
					{
						writer.write(dependency.toString(OutputFormat.VALUE)+' ');
					}					
					writer.write('\n');
					writer.flush();
					System.out.println(i++);
				}

				fileInputStream.close();
				inputStreamReader.close();
				reader.close();

				writer.close();

			} catch (Exception e) {
				e.printStackTrace();
			}
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
	}

// get dependency relation of a sentence
	public static List<TypedDependency> dependency_parse(String sentence) {
		Tokenizer<CoreLabel> tok = tokenizerFactory
				.getTokenizer(new StringReader(sentence));
		List<CoreLabel> rawWords2 = tok.tokenize();
		Tree parse = lp.apply(rawWords2);
		GrammaticalStructure gs = gsf.newGrammaticalStructure(parse);
		return gs.typedDependenciesCCprocessed();
	}

}
