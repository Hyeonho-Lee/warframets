'use strict';
function _instanceof(e, t) {
    return null != t && 'undefined' != typeof Symbol && t[Symbol.hasInstance]
        ? !!t[Symbol.hasInstance](e)
        : e instanceof t;
}
function _classCallCheck(e, t) {
    if (!_instanceof(e, t)) throw new TypeError('Cannot call a class as a function');
}
function _defineProperties(e, t) {
    for (var n = 0; n < t.length; n++) {
        var r = t[n];
        (r.enumerable = r.enumerable || !1),
            (r.configurable = !0),
            'value' in r && (r.writable = !0),
            Object.defineProperty(e, r.key, r);
    }
}
function _createClass(e, t, n) {
    return t && _defineProperties(e.prototype, t), n && _defineProperties(e, n), e;
}
var AutoComplete = (function() {
    function e(t, n) {
        var r = this;
        _classCallCheck(this, e),
            (this.element = t),
            (this.data = n),
            (this.filterData = []),
            (this.checkChoSung = !0),
            this.element.addEventListener('keyup', function() {
                return r.element.value.length
                    ? r._dataFiltering()
                    : (r.element.parentNode.querySelector('ul').style.display = 'none');
            });
    }
    return (
        _createClass(e, [
            {
                key: '_serchResultMake',
                value: function() {
                    var e = this;
                    this.element.parentNode.querySelector('ul') &&
                        this.element.parentNode.removeChild(
                            this.element.parentNode.querySelector('ul')
                        );
                    var t = document.createElement('ul');
                    this.filterData.map(function(n) {
                        for (var r = document.createElement('li'), a = '', l = 0; l < n.length; l++)
                            a +=
                                n[l] === e.element.value[l - n.indexOf(e.element.value)]
                                    ? '<span>'.concat(n[l], '</span>')
                                    : n[l];
                        (r.innerHTML = a), t.appendChild(r);
                        r.className = 'li_count';
                        r.title = e.filterData[t.querySelectorAll('li').length - 1];
                        r.onclick = function() {
                            if (this.location == r.title) {
                                location.href = '/en/result/' + r.title;
                            }
                            location.href = '/en/result/' + r.title;
                        };
                        //console.log(t.querySelectorAll('li').length);
                        //r.title = e.filterData;
                        //console.log(e.filterData[0]);
                        for (var i = 0; i < r.querySelectorAll('span').length; i++)
                            r.querySelectorAll('span')[i].style.color = '#ff7373';
                    }),
                        this.element.parentNode.appendChild(t);
                }
            },
            {
                key: '_dataFiltering',
                value: function() {
                    //여기 수정하면됨
                    var li_get = document.getElementsByClassName('li_count');
                    var ul_get = document.getElementsByClassName('ul_count');
                    /////////////////////////////////////////////
                    
                    var e = this;
                    this._checkChoSung(),
                        (this.filterData = this.data.filter(function(t) {
                            return e._checkInArray(
                                e._toKorChars(t),
                                e._toKorChars(e.element.value)
                            );
                        })),
                        0 === this.filterData.length &&
                            (this.filterData = this.data.filter(function(t) {
                                return (
                                    t.indexOf(e.element.value) >= 0 && e.element.value.length >= 2
                                );
                            })),
                        
                        this.element.value.length
                            ? this._serchResultMake()
                            : (this.element.parentNode.querySelector('ul').style.display = 'none');
(this.element.parentNode.querySelector('ul').className = 'ul_count');
                }
            },
            {
                key: '_checkInArray',
                value: function(e, t) {
                    for (var n = [], r = !0, a = 0; a < t.length; a++) n.push(e[a] === t[a]);
                    for (var l = 0; l < n.length; l++)n[l] || (r = !1);
                    return !!r;
                }
            },
            {
                key: '_checkChoSung',
                value: function() {
                    for (var e, t = this.element.value, n = 0; n < this.element.value.length; n++)
                        32 !== (e = t.charCodeAt(n)) && (this.checkChoSung = !(e < 44032 || e > 55203));
                }
            },
            {
                key: '_toKorChars',
                value: function(e) {
                    for (
                        var t,
                            n,
                            r,
                            a,
                            l = [
                                'a',
                                'b',
                                'c',
                                'd',
                                'e',
                                'f',
                                'g',
                                'h',
                                'i',
                                'j',
                                'k',
                                'l',
                                'm',
                                'n',
                                'o',
                                'p',
                                'q',
                                'r',
                                's',
                                't',
                                'u',
                                'v',
                                'w',
                                'x',
                                'y',
                                'z',
                                'A',
                                'B',
                                'C',
                                'D',
                                'E',
                                'F',
                                'G',
                                'H',
                                'I',
                                'J',
                                'K',
                                'L',
                                'M',
                                'N',
                                'O',
                                'P',
                                'Q',
                                'R',
                                'S',
                                'T',
                                'Y',
                                'V',
                                'W',
                                'X',
                                'Y',
                                'Z'
                            ],
                            i = [
                                'a',
                                'b',
                                'c',
                                'd',
                                'e',
                                'f',
                                'g',
                                'h',
                                'i',
                                'j',
                                'k',
                                'l',
                                'm',
                                'n',
                                'o',
                                'p',
                                'q',
                                'r',
                                's',
                                't',
                                'u',
                                'v',
                                'w',
                                'x',
                                'y',
                                'z',
                                'A',
                                'B',
                                'C',
                                'D',
                                'E',
                                'F',
                                'G',
                                'H',
                                'I',
                                'J',
                                'K',
                                'L',
                                'M',
                                'N',
                                'O',
                                'P',
                                'Q',
                                'R',
                                'S',
                                'T',
                                'Y',
                                'V',
                                'W',
                                'X',
                                'Y',
                                'Z'
                            ],
                            o = [
                                'a',
                                'b',
                                'c',
                                'd',
                                'e',
                                'f',
                                'g',
                                'h',
                                'i',
                                'j',
                                'k',
                                'l',
                                'm',
                                'n',
                                'o',
                                'p',
                                'q',
                                'r',
                                's',
                                't',
                                'u',
                                'v',
                                'w',
                                'x',
                                'y',
                                'z',
                                'A',
                                'B',
                                'C',
                                'D',
                                'E',
                                'F',
                                'G',
                                'H',
                                'I',
                                'J',
                                'K',
                                'L',
                                'M',
                                'N',
                                'O',
                                'P',
                                'Q',
                                'R',
                                'S',
                                'T',
                                'Y',
                                'V',
                                'W',
                                'X',
                                'Y',
                                'Z'
                            ],
                            h = e,
                            s = h.length,
                            u = [],
                            c = [],
                            f = 0;
                        f < s;
                        f++
                    )
                        32 !== (a = h.charCodeAt(f)) &&
                            (a < 44032 || a > 55203
                                ? (u.push(h.charAt(f)), c.push(h.charAt(f)))
                                : ((t =
                                      (((a = h.charCodeAt(f) - 44032) - (r = a % 28)) / 28 -
                                          (n = ((a - r) / 28) % 21)) /
                                      21),
                                  u.push(l[t], i[n]),
                                  c.push(l[t]),
                                  '' !== o[r] && u.push(o[r])));
                    return this.checkChoSung ? u : c;
                }
            }
        ]),
        e
    );
})();