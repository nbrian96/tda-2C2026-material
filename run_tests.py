"""Script unificado de ejecución para todas las suites de prueba: unitarias, integración y auditoría QA."""

import os
import sys
import unittest

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    print("=" * 70)
    print("EJECUTANDO SUITE COMPLETA DE PRUEBAS DE TDA (UNIT + INTEGRATION + QA)")
    print("=" * 70)

    loader = unittest.TestLoader()
    suite = loader.discover(os.path.join(BASE_DIR, "tests"), pattern="test_*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print(f"TODAS LAS PRUEBAS PASARON ({result.testsRun} tests ejecutados exitosamente)")
        print("=" * 70)
        return 0
    else:
        print(f"FALLARON PRUEBAS: {len(result.failures)} fallos, {len(result.errors)} errores")
        print("=" * 70)
        return 1

if __name__ == "__main__":
    sys.exit(main())
