@Library('libpipelines') _

hose {
    EMAIL = 'genai'
    DEVTIMEOUT = 60
    RELEASETIMEOUT = 60
    BUILDTOOL = 'make'
    BUILDTOOL_IMAGE = 'stratio/python-builder-3.9:1.0.0'
    BUILDTOOL_CPU_LIMIT = '8'
    BUILDTOOL_CPU_REQUEST = '2'
    PYTHON_MODULE = true
    GRYPE_TEST = false
    LABEL_CONTROL = true
    DEPLOYONPRS = true

    DEV = { config ->
        doCompile(config)
        doUT(config)
        doStaticAnalysis(
            conf: config,
            sonarAdditionalProperties: [
                "sonar.language": "py",
                "sonar.python.version": "3.9",
                "sonar.sources": ".",
                "sonar.exclusions": "*/tests/**,*/scripts/**,*/pytest-coverage.xml",
                "sonar.tests": ".",
                "sonar.test.inclusions": "*/tests/**",
                "sonar.python.coverage.reportPaths": "genai-chain-examples/pytest-coverage.xml,genai-chain-docs/pytest-coverage.xml",
                "sonar.python.pylint.reportPaths": "genai-chain-examples/pylint-report.txt,genai-chain-docs/pylint-report.txt",
                "sonar.scm.disabled": "true"
            ])
        doPackage(config)
        doDeploy(config)
    }
}