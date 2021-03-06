import re
import unittest
from CompilationEngine import CompilationEngine

class CompilationEngineTest(unittest.TestCase):
    def test_compile_class(self):
        engine = CompilationEngine("BasicTestClass.jack", "fakeOutputFile")
        engine.compile_class()
        self.assertEqual(engine.output, [
            '<class>',
                '<keyword> class </keyword>',
                '<identifier> BasicTestClass </identifier>',
                '<symbol> { </symbol>',
                '<symbol> } </symbol>',
            '</class>'])

    def test_compile_class_var_dec(self):
        engine = CompilationEngine("field int direction;", "fakeOutputFile", True)
        engine.compile_class_var_dec()
        self.assertEqual(engine.output, [
            '<classVarDec>',
                '<keyword> field </keyword>',
                '<keyword> int </keyword>',
                '<identifier> direction </identifier>',
                '<symbol> ; </symbol>',
            '</classVarDec>'])

    def test_compile_class_var_dec_2(self):
        engine = CompilationEngine("field int directionA, directionB;", "fakeOutputFile", True)
        engine.compile_class_var_dec()
        self.assertEqual(engine.output, [
            '<classVarDec>',
                '<keyword> field </keyword>',
                '<keyword> int </keyword>',
                '<identifier> directionA </identifier>',
                '<symbol> , </symbol>',
                '<identifier> directionB </identifier>',
                '<symbol> ; </symbol>',
            '</classVarDec>'])


    def test_compile_subroutine_dec(self):
        engine = CompilationEngine("method void decSize(int Ax, int Ay) { var boolean exit; }", "fakeOutputFile", True)
        engine.compile_subroutine_dec()
        self.assertEqual(engine.output, [
            '<subroutineDec>',
                '<keyword> method </keyword>',
                '<keyword> void </keyword>',
                '<identifier> decSize </identifier>',
                '<symbol> ( </symbol>',
                '<parameterList>',
                    '<keyword> int </keyword>',
                    '<identifier> Ax </identifier>',
                    '<symbol> , </symbol>',
                    '<keyword> int </keyword>',
                    '<identifier> Ay </identifier>',
                '</parameterList>',
                '<symbol> ) </symbol>',
                '<subroutineBody>',
                    '<symbol> { </symbol>',
                    '<varDec>',
                        '<keyword> var </keyword>',
                        '<keyword> boolean </keyword>',
                        '<identifier> exit </identifier>',
                        '<symbol> ; </symbol>',
                    '</varDec>',
                    '<statements>',
                    '</statements>',
                    '<symbol> } </symbol>',
                '</subroutineBody>',
            '</subroutineDec>'])

    def test_compile_var_dec(self):
        engine = CompilationEngine("var char key;", "fakeOutputFile", True)
        engine.compile_var_dec()
        self.assertEqual(engine.output, [
            '<varDec>',
                '<keyword> var </keyword>',
                '<keyword> char </keyword>',
                '<identifier> key </identifier>',
                '<symbol> ; </symbol>',
            '</varDec>'])

    def test_compile_var_dec_2(self):
        engine = CompilationEngine("var char keyA, keyB;", "fakeOutputFile", True)
        engine.compile_var_dec()
        self.assertEqual(engine.output, [
            '<varDec>',
                '<keyword> var </keyword>',
                '<keyword> char </keyword>',
                '<identifier> keyA </identifier>',
                '<symbol> , </symbol>',
                '<identifier> keyB </identifier>',
                '<symbol> ; </symbol>',
            '</varDec>'])

    def test_compile_let(self):
        engine = CompilationEngine('let x = "string constant";', "fakeOutputFile", True)
        engine.compile_let()
        self.assertEqual(engine.output, [
            '<letStatement>',
                '<keyword> let </keyword>',
                '<identifier> x </identifier>',
                '<symbol> = </symbol>',
                '<expression>',
                    '<term>',
                        '<stringConstant> string constant </stringConstant>',
                    '</term>',
                '</expression>',
                '<symbol> ; </symbol>',
            '</letStatement>'])

    def test_compile_if(self):
        engine = CompilationEngine("if (key = 81) { return; } else {}", "fakeOutputFile", True)
        engine.compile_if()
        self.assertEqual(engine.output, [
            '<ifStatement>',
                '<keyword> if </keyword>',
                '<symbol> ( </symbol>',
                '<expression>',
                    '<term>',
                        '<identifier> key </identifier>',
                    '</term>',
                    '<symbol> = </symbol>',
                    '<term>',
                        '<integerConstant> 81 </integerConstant>',
                    '</term>',
                '</expression>',
                '<symbol> ) </symbol>',
                '<symbol> { </symbol>',
                '<statements>',
                    '<returnStatement>',
                        '<keyword> return </keyword>',
                        '<symbol> ; </symbol>',
                    '</returnStatement>',
                '</statements>',
                '<symbol> } </symbol>',
                '<keyword> else </keyword>',
                '<symbol> { </symbol>',
                '<statements>',
                '</statements>',
                '<symbol> } </symbol>',
            '</ifStatement>'])

    def test_compile_while(self):
        engine = CompilationEngine("while (key = 0) {}", "fakeOutputFile", True)
        engine.compile_while()
        self.assertEqual(engine.output, [
            '<whileStatement>',
                '<keyword> while </keyword>',
                '<symbol> ( </symbol>',
                '<expression>',
                    '<term>',
                        '<identifier> key </identifier>',
                    '</term>',
                    '<symbol> = </symbol>',
                    '<term>',
                        '<integerConstant> 0 </integerConstant>',
                    '</term>',
                '</expression>',
                '<symbol> ) </symbol>',
                '<symbol> { </symbol>',
                '<statements>',
                '</statements>',
                '<symbol> } </symbol>',
            '</whileStatement>'])

    def test_compile_do(self):
        engine = CompilationEngine("do draw();", "fakeOutputFile", True)
        engine.compile_do()
        self.assertEqual(engine.output, [
            '<doStatement>',
                '<keyword> do </keyword>',
                '<identifier> draw </identifier>',
                '<symbol> ( </symbol>',
                '<expressionList>',
                '</expressionList>',
                '<symbol> ) </symbol>',
                '<symbol> ; </symbol>',
            '</doStatement>'])

    def test_compile_do_2(self):
        engine = CompilationEngine("do square.dispose();", "fakeOutputFile", True)
        engine.compile_do()
        self.assertEqual(engine.output, [
            '<doStatement>',
                '<keyword> do </keyword>',
                '<identifier> square </identifier>',
                '<symbol> . </symbol>',
                '<identifier> dispose </identifier>',
                '<symbol> ( </symbol>',
                '<expressionList>',
                '</expressionList>',
                '<symbol> ) </symbol>',
                '<symbol> ; </symbol>',
            '</doStatement>'])

    def test_compile_return(self):
        engine = CompilationEngine("return;", "fakeOutputFile", True)
        engine.compile_return()
        self.assertEqual(engine.output, [
            '<returnStatement>',
                '<keyword> return </keyword>',
                '<symbol> ; </symbol>',
            '</returnStatement>'])

    def test_compile_return_2(self):
        engine = CompilationEngine("return this;", "fakeOutputFile", True)
        engine.compile_return()
        self.assertEqual(engine.output, [
            '<returnStatement>',
                '<keyword> return </keyword>',
                '<expression>',
                    '<term>',
                        '<keyword> this </keyword>',
                    '</term>',
                '</expression>',
                '<symbol> ; </symbol>',
            '</returnStatement>'])

    def test_square_main_file(self):
        engine = CompilationEngine("../Square/Main.jack", "fakeOutputFile")
        engine.compile_class()
        xml_file = self.convert_xml_file("../Square/Main.xml")
        self.assertEqual(len(engine.output), 244)
        self.assertEqual(engine.output, xml_file)

    def test_square_file(self):
        engine = CompilationEngine("../Square/Square.jack", "fakeOutputFile")
        engine.compile_class()
        xml_file = self.convert_xml_file("../Square/Square.xml")
        self.assertEqual(len(engine.output), 1211)
        self.assertEqual(engine.output, xml_file)

    def test_square_game_file(self):
        engine = CompilationEngine("../Square/SquareGame.jack", "fakeOutputFile")
        engine.compile_class()
        xml_file = self.convert_xml_file("../Square/SquareGame.xml")
        self.assertEqual(len(engine.output), 643)
        self.assertEqual(engine.output, xml_file)

    def convert_xml_file(self, filepath):
        file_text = open(filepath, 'r').read()
        file_text_in_array = file_text.split('\n')
        result = []
        for line in file_text_in_array:
            if len(line) == 0:
                continue
            result.append(line.strip())
        return result
