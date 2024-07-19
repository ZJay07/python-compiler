python_library (
    name = "lexing",
    srcs = ["main/lexer.py"],
    visibility = ["//src/..."],
    deps = [
        "//third_party/python:ply",
    ],
)

python_library (
    name = "parser",
    srcs = ["main/parser.py"],
    visibility = ["//src/..."],
    deps = [
        "//third_party/python:ply",
    ],
)

python_test (
    name = "lexer_test",
    srcs = ["test/test_lexer.py"],
    deps = [
        ":lexing",
    ],
)

python_test (
    name = "parser_test",
    srcs = ["test/test_parser.py"],
    deps = [
        ":parser",
    ],
)
