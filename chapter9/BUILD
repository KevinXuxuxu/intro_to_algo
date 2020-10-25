package(default_visibility = ["//visibility:public"])

py_library(
    name = "quick_select",
    srcs = [
        "quick_select.py",
    ],
    deps = [
        "//chapter7:quick_sort",
    ],
)

py_test(
    name = "quick_select_test",
    srcs = [
        "quick_select_test.py",
    ],
    data = [
        "//test:random_sort_test_cases",
    ],
    deps = [
        ":quick_select"
    ],
)
