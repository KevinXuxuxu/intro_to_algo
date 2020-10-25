package(default_visibility = ["//visibility:public"])

filegroup(
    name = "random_sort_test_cases",
    srcs = glob([
        "random_sort_test_cases.json"
    ]),
)

py_test(
    name = "sort_test",
    srcs = [
        "sort_test.py",
    ],
    data = [
        ":random_sort_test_cases",
    ],
    deps = [
        "//chapter2:insertion_sort",
        "//chapter2:merge_sort",
        "//chapter6:heap_sort",
        "//chapter7:quick_sort",
        "//chapter8:counting_sort",
        "//chapter8:radix_sort",
    ],
)
