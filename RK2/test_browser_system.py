import unittest
from refactored_code import (
    Computer, Browser, BrowserComputer,
    has_russian_ov_ending,
    query1_browsers_with_ov_ending,
    query2_computers_avg_memory,
    query3_computers_starting_with_a
)


class TestBrowserSystem(unittest.TestCase):
    
    def setUp(self):
        self.computers = [
            Computer(1, "Dell XPS 15"),
            Computer(2, "HP Pavilion"),
            Computer(3, "Lenovo ThinkPad"),
            Computer(4, "Asus ROG"),
            Computer(5, "Acer Aspire")
        ]
        
        self.browsers = [
            Browser(1, "Chrome", 450, 1),
            Browser(2, "Firefox", 320, 1),
            Browser(3, "Edge", 280, 2),
            Browser(4, "Safari", 350, 3),
            Browser(5, "Opera", 180, 3),
            Browser(6, "Chrome", 420, 4),
            Browser(7, "Firefox", 300, 5),
            Browser(8, "Иванов Браузер", 250, 2),
            Browser(9, "Петров Навигатор", 190, 4),
            Browser(10, "Сидоров Обозреватель", 220, 1),
            Browser(11, "Google Chrome", 400, 2)
        ]
        
        self.browser_computers = [
            BrowserComputer(1, 1),
            BrowserComputer(2, 1),
            BrowserComputer(3, 2),
            BrowserComputer(4, 3),
            BrowserComputer(5, 3),
            BrowserComputer(6, 4),
            BrowserComputer(7, 5),
            BrowserComputer(8, 2),
            BrowserComputer(9, 4),
            BrowserComputer(10, 1),
            BrowserComputer(11, 2),
            BrowserComputer(1, 2),
            BrowserComputer(3, 1),
            BrowserComputer(5, 4),
            BrowserComputer(7, 3),
        ]
    
    def test_has_russian_ov_ending(self):
        self.assertTrue(has_russian_ov_ending("Иванов Браузер"))
        self.assertTrue(has_russian_ov_ending("Петров Навигатор"))
        self.assertTrue(has_russian_ov_ending("Сидоров Обозреватель"))
        self.assertTrue(has_russian_ov_ending("Сергеев Эксплоров"))
        
        self.assertFalse(has_russian_ov_ending("Chrome"))
        self.assertFalse(has_russian_ov_ending("Firefox"))
        self.assertFalse(has_russian_ov_ending("Microsoft Edge"))
        self.assertFalse(has_russian_ov_ending("Google Chrome"))
        
        self.assertTrue(has_russian_ov_ending("ИВАНОВ БРАУЗЕР"))
        self.assertTrue(has_russian_ov_ending("петров навигатор"))
    
    def test_query1_browsers_with_ov_ending(self):
        result = query1_browsers_with_ov_ending(self.browsers, self.computers)
        
        self.assertEqual(len(result), 3)
        
        browser_names = [browser.name for browser, _ in result]
        expected_names = ["Иванов Браузер", "Петров Навигатор", "Сидоров Обозреватель"]
        
        for name in browser_names:
            self.assertTrue(has_russian_ov_ending(name))
        
        computer_models = [computer.model for _, computer in result]
        self.assertIn("HP Pavilion", computer_models)
        self.assertIn("Asus ROG", computer_models)
        self.assertIn("Dell XPS 15", computer_models)
    
    def test_query2_computers_avg_memory(self):
        result = query2_computers_avg_memory(self.browsers, self.computers)
        
        self.assertEqual(len(result), 5)
        
        avg_memories = [avg_memory for _, avg_memory in result]
        self.assertEqual(avg_memories, sorted(avg_memories))
        
        dell_result = next((item for item in result if item[0] == "Dell XPS 15"), None)
        self.assertIsNotNone(dell_result)
        self.assertAlmostEqual(dell_result[1], 330.0, places=2)
        
        acer_result = next((item for item in result if item[0] == "Acer Aspire"), None)
        self.assertIsNotNone(acer_result)
        self.assertAlmostEqual(acer_result[1], 300.0, places=2)
    
    def test_query3_computers_starting_with_a(self):
        result = query3_computers_starting_with_a(
            self.browsers, self.computers, self.browser_computers
        )
        
        self.assertEqual(len(result), 2)
        
        computer_models = [computer.model for computer, _ in result]
        self.assertEqual(computer_models, sorted(computer_models))
        
        expected_models = ["Acer Aspire", "Asus ROG"]
        actual_models = [model for model in computer_models]
        self.assertEqual(actual_models, expected_models)
        
        asus_result = next((item for item in result if item[0].model == "Asus ROG"), None)
        self.assertIsNotNone(asus_result)
        asus_computer, asus_browsers = asus_result
        
        browser_names = [browser.name for browser in asus_browsers]
        self.assertIn("Chrome", browser_names)
        self.assertIn("Петров Навигатор", browser_names)
        self.assertIn("Opera", browser_names)


if __name__ == "__main__":
    unittest.main(verbosity=2)