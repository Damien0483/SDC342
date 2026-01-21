---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[1], line 40
     37 y = df["price_category"]
     39 # Train-test split (80/20)
---> 40 X_train, X_test, y_train, y_test = train_test_split(
     41     X, y, test_size=0.20, random_state=42, stratify=y
     42 )
     44 display(Markdown("### Features"))
     45 display(X.head())

File C:\Program Files\Python311\Lib\site-packages\sklearn\utils\_param_validation.py:211, in validate_params.<locals>.decorator.<locals>.wrapper(*args, **kwargs)
    205 try:
    206     with config_context(
    207         skip_parameter_validation=(
    208             prefer_skip_nested_validation or global_skip_validation
    209         )
    210     ):
--> 211         return func(*args, **kwargs)
    212 except InvalidParameterError as e:
    213     # When the function is just a wrapper around an estimator, we allow
    214     # the function to delegate validation to the estimator, but we replace
    215     # the name of the estimator by the name of the function in the error
    216     # message to avoid confusion.
    217     msg = re.sub(
    218         r"parameter of \w+ must be",
    219         f"parameter of {func.__qualname__} must be",
    220         str(e),
    221     )

File C:\Program Files\Python311\Lib\site-packages\sklearn\model_selection\_split.py:2638, in train_test_split(test_size, train_size, random_state, shuffle, stratify, *arrays)
   2634         CVClass = ShuffleSplit
   2636     cv = CVClass(test_size=n_test, train_size=n_train, random_state=random_state)
-> 2638     train, test = next(cv.split(X=arrays[0], y=stratify))
   2640 return list(
   2641     chain.from_iterable(
   2642         (_safe_indexing(a, train), _safe_indexing(a, test)) for a in arrays
   2643     )
   2644 )

File C:\Program Files\Python311\Lib\site-packages\sklearn\model_selection\_split.py:2197, in StratifiedShuffleSplit.split(self, X, y, groups)
   2163 def split(self, X, y, groups=None):
   2164     """Generate indices to split data into training and test set.
   2165 
   2166     Parameters
   (...)
   2195     to an integer.
   2196     """
-> 2197     y = check_array(y, input_name="y", ensure_2d=False, dtype=None)
   2198     return super().split(X, y, groups)

File C:\Program Files\Python311\Lib\site-packages\sklearn\utils\validation.py:959, in check_array(array, accept_sparse, accept_large_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, ensure_min_samples, ensure_min_features, estimator, input_name)
    953         raise ValueError(
    954             "Found array with dim %d. %s expected <= 2."
    955             % (array.ndim, estimator_name)
    956         )
    958     if force_all_finite:
--> 959         _assert_all_finite(
    960             array,
    961             input_name=input_name,
    962             estimator_name=estimator_name,
    963             allow_nan=force_all_finite == "allow-nan",
    964         )
    966 if ensure_min_samples > 0:
    967     n_samples = _num_samples(array)

File C:\Program Files\Python311\Lib\site-packages\sklearn\utils\validation.py:109, in _assert_all_finite(X, allow_nan, msg_dtype, estimator_name, input_name)
    107 if X.dtype == np.dtype("object") and not allow_nan:
    108     if _object_dtype_isnan(X).any():
--> 109         raise ValueError("Input contains NaN")
    111 # We need only consider float arrays, hence can early return for all else.
    112 if not xp.isdtype(X.dtype, ("real floating", "complex floating")):

ValueError: Input contains NaN
