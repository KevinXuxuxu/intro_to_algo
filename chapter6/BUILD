package(default_visibility = ["//visibility:public"])

py_library(
    name = "my_heap",
    srcs = [
        "my_heap.py",
    ],
    deps = [
        "//utils:sort_utils",
    ],
)

py_test(
    name = "my_heap_test",
    srcs = [
        "my_heap_test.py",
    ],
    deps = [
        ":my_heap",
        "//utils:sort_utils",
    ],
)

py_library(
    name = "heap_sort",
    srcs = [
        "heap_sort.py",
    ],
    deps = [
        ":my_heap",
    ]
)

py_library(
    name = "my_priority_queue",
    srcs = [
        "my_priority_queue.py",
    ]
)

py_test(
    name = "my_priority_queue_test",
    srcs = [
        "my_priority_queue_test.py",
    ],
    deps = [
        ":my_priority_queue",
    ],
)
