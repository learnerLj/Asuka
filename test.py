import unittest

class TestScanner(unittest.TestCase):

    def test_ast_scanner(self):
        from solidity_antlr4_parser.parser import parse_file, objectify
        from ast_scanner.ast_scanner import Scanner
        path = "/Users/wang/dev/Asuka/test_data/test.sol"
        source_unit = parse_file(path, loc=True)
        source_unit_object = objectify(source_unit, path)
        scanner = Scanner(source_unit_object)
        pass
    
class TestVuls(unittest.TestCase):
    
    def test_int_overflow(self):
        from solidity_antlr4_parser.parser import parse_file, objectify
        from ast_scanner.ast_scanner import Scanner
        from vuls.int_overflow import check
        path = "/Users/wang/dev/Asuka/test.sol"
        source_unit = parse_file(path, loc=True)
        source_unit_object = objectify(source_unit, path)
        scanner = Scanner(source_unit_object)
        vuls = check(scanner)
        pass
    
    def test_check_solc_version(self):
        from vuls.utils import check_solc_version
        self.assertEqual(True, check_solc_version("<=0.8.0", 8))
        self.assertEqual(False, check_solc_version("^0.8.0", 8))
        self.assertEqual(False, check_solc_version("0.8.0", 8))
        self.assertEqual(True, check_solc_version("<0.8.0", 8))
        self.assertEqual(True, check_solc_version("<0.7.0", 8))
        self.assertEqual(True, check_solc_version("^0.7.0", 8))
        self.assertEqual(True, check_solc_version("0.4.0", 8))
        
    def test_function_default_visibility(self):
        from solidity_antlr4_parser.parser import parse_file, objectify
        from ast_scanner.ast_scanner import Scanner
        from vuls.function_default_visibility import check
        path = "/Users/wang/dev/Asuka/test1.sol"
        source_unit = parse_file(path, loc=True)
        source_unit_object = objectify(source_unit, path)
        scanner = Scanner(source_unit_object)
        vuls = check(scanner)
        pass
    
    def test_unchecked_return_value(self):
        from solidity_antlr4_parser.parser import parse_file, objectify
        from ast_scanner.ast_scanner import Scanner
        from vuls.unchecked_return_value import check
        path = "/Users/wang/dev/Asuka/test1.sol"
        source_unit = parse_file(path, loc=True)
        source_unit_object = objectify(source_unit, path)
        scanner = Scanner(source_unit_object)
        vuls = check(scanner)
        pass
    
    def test_reentrancy(self):
        from solidity_antlr4_parser.parser import parse_file, objectify
        from ast_scanner.ast_scanner import Scanner
        from vuls.reentrancy import check
        path = "/Users/wang/dev/Asuka/test_data/reentrancy.sol"
        source_unit = parse_file(path, loc=True)
        source_unit_object = objectify(source_unit, path)
        scanner = Scanner(source_unit_object)
        vuls = check(scanner)
        pass
    
    def test_access_of_uninitialized_pointer(self):
        from solidity_antlr4_parser.parser import parse_file, objectify
        from ast_scanner.ast_scanner import Scanner
        from vuls.access_of_uninitialized_pointer import check
        path = "/Users/wang/dev/Asuka/test_data/access_of_uninitialized_pointer.sol"
        source_unit = parse_file(path, loc=True)
        source_unit_object = objectify(source_unit, path)
        scanner = Scanner(source_unit_object)
        vuls = check(scanner)
        pass
    
    def test_tx_origin(self):
        from solidity_antlr4_parser.parser import parse_file, objectify
        from ast_scanner.ast_scanner import Scanner
        from vuls.tx_origin import check
        path = "/Users/wang/dev/Asuka/test_data/tx_origin.sol"
        source_unit = parse_file(path, loc=True)
        source_unit_object = objectify(source_unit, path)
        scanner = Scanner(source_unit_object)
        vuls = check(scanner)
        pass
    
    def test_get_all_detector(self):
        from vuls import all_detector
        detectorList = [
            getattr(all_detector, attrName) 
            for attrName in dir(all_detector) 
            if hasattr(getattr(all_detector, attrName), "check")
        ]
        pass
    
    
class TestAuaka(unittest.TestCase):
    
    def test_asuka_class(self):
        from core.asuka import Asuka
        root = "test_data"
        asuka = Asuka(_root=root)
        fileNum = asuka.file_count()
        asuka.scan()
        vulNum = asuka.vul_count()
        table = asuka.vulTable
        pass
    
    
class TestPrinter(unittest.TestCase):
    
    def test_print_banner(self):
        from core.printer import Printer
        Printer.print_banner()
        
        
class TestMain(unittest.TestCase):
    
    def test_parse_vuls_string(self):
        from core.__main__ import parse_vuls_string
        text1 = "s100,101,107,s115"
        vuls1 = parse_vuls_string(text1)
        text2 = "asdf,199,s111,234123"
        vuls2 = parse_vuls_string(text2)