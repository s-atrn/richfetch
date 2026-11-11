import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import richfetch


class RichfetchHostnameTests(unittest.TestCase):
    def test_get_system_info_runs_on_platforms_without_os_uname(self) -> None:
        with patch.object(sys, "argv", ["richfetch"]):
            info = richfetch.get_system_info()
        self.assertIsInstance(info, dict)
        self.assertTrue(info)


if __name__ == "__main__":
    unittest.main()
