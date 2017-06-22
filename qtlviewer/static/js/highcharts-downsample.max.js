
(function (H) {
    "use strict";

    if(!Array.isArray) {
        Array.isArray = function (vArg) {
            return Object.prototype.toString.call(vArg) === "[object Array]";
        };
    }

function range$1 (start, stop, step) {
    start = +start, stop = +stop, step = (n = arguments.length) < 2 ? (stop = start, start = 0, 1) : n < 3 ? 1 : +step;

    var i = -1,
        n = Math.max(0, Math.ceil((stop - start) / step)) | 0,
        range = new Array(n);

    while (++i < n) {
      range[i] = start + i * step;
    }

    return range;
  }
  
  
  

  function ascending (a, b) {
    return a < b ? -1 : a > b ? 1 : a >= b ? 0 : NaN;
  }

  function bisector (compare) {
    if (compare.length === 1) compare = ascendingComparator(compare);
    return {
      left: function left(a, x, lo, hi) {
        if (lo == null) lo = 0;
        if (hi == null) hi = a.length;
        while (lo < hi) {
          var mid = lo + hi >>> 1;
          if (compare(a[mid], x) < 0) lo = mid + 1;else hi = mid;
        }
        return lo;
      },
      right: function right(a, x, lo, hi) {
        if (lo == null) lo = 0;
        if (hi == null) hi = a.length;
        while (lo < hi) {
          var mid = lo + hi >>> 1;
          if (compare(a[mid], x) > 0) hi = mid;else lo = mid + 1;
        }
        return lo;
      }
    };
  }

  function ascendingComparator(f) {
    return function (d, x) {
      return ascending(f(d), x);
    };
  }

  var ascendingBisect = bisector(ascending);

  function number (x) {
    return x === null ? NaN : +x;
  }

  function extent (array, f) {
    var i = -1,
        n = array.length,
        a,
        b,
        c;

    if (f == null) {
      while (++i < n) {
        if ((b = array[i]) != null && b >= b) {
          a = c = b;break;
        }
      }while (++i < n) {
        if ((b = array[i]) != null) {
          if (a > b) a = b;
          if (c < b) c = b;
        }
      }
    } else {
      while (++i < n) {
        if ((b = f(array[i], i, array)) != null && b >= b) {
          a = c = b;break;
        }
      }while (++i < n) {
        if ((b = f(array[i], i, array)) != null) {
          if (a > b) a = b;
          if (c < b) c = b;
        }
      }
    }

    return [a, c];
  }

  function range$1 (start, stop, step) {
    start = +start, stop = +stop, step = (n = arguments.length) < 2 ? (stop = start, start = 0, 1) : n < 3 ? 1 : +step;

    var i = -1,
        n = Math.max(0, Math.ceil((stop - start) / step)) | 0,
        range = new Array(n);

    while (++i < n) {
      range[i] = start + i * step;
    }

    return range;
  }

  function max (array, f) {
    var i = -1,
        n = array.length,
        a,
        b;

    if (f == null) {
      while (++i < n) {
        if ((b = array[i]) != null && b >= b) {
          a = b;break;
        }
      }while (++i < n) {
        if ((b = array[i]) != null && b > a) a = b;
      }
    } else {
      while (++i < n) {
        if ((b = f(array[i], i, array)) != null && b >= b) {
          a = b;break;
        }
      }while (++i < n) {
        if ((b = f(array[i], i, array)) != null && b > a) a = b;
      }
    }

    return a;
  }
var regexify = (function (strsOrRegexes) {
      return strsOrRegexes.map(function (strOrRegex) {
          return typeof strOrRegex === 'string' ? new RegExp('^' + strOrRegex + '$') : strOrRegex;
      });
  });

  var include = (function () {
      for (var _len = arguments.length, inclusions = Array(_len), _key = 0; _key < _len; _key++) {
          inclusions[_key] = arguments[_key];
      }

      inclusions = regexify(inclusions);
      return function (name) {
          return inclusions.some(function (inclusion) {
              return inclusion.test(name);
          }) && name;
      };
  });

  var createTransform = function createTransform(transforms) {
      return function (name) {
          return transforms.reduce(function (name, fn) {
              return name && fn(name);
          }, name);
      };
  };

  var createReboundMethod = function createReboundMethod(target, source, name) {
      var method = source[name];
      if (typeof method !== 'function') {
          throw new Error('Attempt to rebind ' + name + ' which isn\'t a function on the source object');
      }
      return function () {
          for (var _len = arguments.length, args = Array(_len), _key = 0; _key < _len; _key++) {
              args[_key] = arguments[_key];
          }

          var value = method.apply(source, args);
          return value === source ? target : value;
      };
  };

  var rebindAll = (function (target, source) {
      for (var _len2 = arguments.length, transforms = Array(_len2 > 2 ? _len2 - 2 : 0), _key2 = 2; _key2 < _len2; _key2++) {
          transforms[_key2 - 2] = arguments[_key2];
      }

      var transform = createTransform(transforms);
      var _iteratorNormalCompletion = true;
      var _didIteratorError = false;
      var _iteratorError = undefined;

      try {
          for (var _iterator = Object.keys(source)[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
              var name = _step.value;

              var result = transform(name);
              if (result) {
                  target[result] = createReboundMethod(target, source, name);
              }
          }
      } catch (err) {
          _didIteratorError = true;
          _iteratorError = err;
      } finally {
          try {
              if (!_iteratorNormalCompletion && _iterator.return) {
                  _iterator.return();
              }
          } finally {
              if (_didIteratorError) {
                  throw _iteratorError;
              }
          }
      }

      return target;
  });

  var rebind = (function (target, source) {
      for (var _len = arguments.length, names = Array(_len > 2 ? _len - 2 : 0), _key = 2; _key < _len; _key++) {
          names[_key - 2] = arguments[_key];
      }

      return rebindAll(target, source, include.apply(undefined, names));
  });


  function bucket () {

      var bucketSize = 10;

      var bucket = function bucket(data) {
          return range$1(0, Math.ceil(data.length / bucketSize)).map(function (i) {
              return data.slice(i * bucketSize, (i + 1) * bucketSize);
          });
      };

      bucket.bucketSize = function (x) {
          if (!arguments.length) {
              return bucketSize;
          }

          bucketSize = x;
          return bucket;
      };

      return bucket;
  }

  
function modeMax () {
      var dataBucketer = bucket();
      var value = function value(d) {
          return d;
      };

      var modeMax = function modeMax(data) {
          if (dataBucketer.bucketSize() > data.length) {
              return data;
          }

          var minMax = extent(data, value);
          var buckets = dataBucketer(data.slice(1, data.length - 1));

          var subsampledData = buckets.map(function (thisBucket, i) {
              var values = thisBucket.map(value);
              //console.log(values);
              var maxValue = max(values);
              return thisBucket[values.indexOf(maxValue)];

          });

          // First and last data points are their own buckets.
          return [].concat(data[0], subsampledData, data[data.length - 1]);
      };

      rebind(modeMax, dataBucketer, 'bucketSize');

      modeMax.value = function (x) {
          if (!arguments.length) {
              return value;
          }

          value = x;

          return modeMax;
      };

      return modeMax;
  }


    H.wrap(H.Series.prototype, 'setData', function (proceed) {
        var opt = this.options;
        if (opt.hasOwnProperty('downsample')) {

            if (opt.downsample.threshold != 0) {

                // Bucket size. Leave room for start and end data points
                var bs = (arguments[1].length - 2) / (opt.downsample.threshold - 2);


                //console.log('arguments[1]=', arguments[1]);
                var sampler = modeMax()
                    .bucketSize(bs)
                    .value(function(d) { return d['y']; });


                    
                arguments[1] = sampler(arguments[1]);

                //console.log('arguments[1].length=', arguments[1].length);
            }

            /*
 
            if (Array.isArray(arguments[1][0]) && arguments[1][0].length == 2) {
                // Data is array of arrays with two values
                arguments[1] = largestTriangleThreeBuckets(arguments[1], opt.downsample.threshold);
            } else if (!isNaN(parseFloat(arguments[1][0])) && isFinite(arguments[1][0])) {
                // Data is array of numerical values.
                var point_x = typeof opt.pointStart != 'undefined' ? opt.pointStart : 0; // First X
                var pointInterval = typeof opt.pointInterval != 'undefined' ? opt.pointInterval : 1;
                // Turn it into array of arrays with two values.
                for (var i = 0, len = arguments[1].length; i < len; i++) {
                    arguments[1][i] = [point_x, arguments[1][i]];
                    point_x += pointInterval;
                }
                arguments[1] = largestTriangleThreeBuckets(arguments[1], opt.downsample.threshold);
            } else {
                console.log("Downsample Error: Invalid data format! Note: Array of objects and Range Series are not supported");
            }
            */
        }
        proceed.apply(this, Array.prototype.slice.call(arguments, 1));
    });

}(Highcharts));