"""
© 2024 Stratio Big Data Inc., Sucursal en España. All rights reserved.

This software – including all its source code – contains proprietary
information of Stratio Big Data Inc., Sucursal en España and
may not be revealed, sold, transferred, modified, distributed or
otherwise made available, licensed or sublicensed to third parties;
nor reverse engineered, disassembled or decompiled, without express
written authorization from Stratio Big Data Inc., Sucursal en España.
"""
from genai_core.server.server import GenAiServer


def main():
    app = GenAiServer(
        module_name="genai_chain_echo.chain",
        class_name="EchoChain",
        config={},
    )
    app.start_server()


if __name__ == "__main__":
    main()