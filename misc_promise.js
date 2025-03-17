class Promisify {
    constructor(fn) {
        this._thenFns = [];
        fn(this._resolve.bind(this));
    }
    then(fn) {
        let resolver;
        const p = new Promisify(resolve => {
            resolver = resolve;
        });
        this._thenFns.push((result) => {
            resolver(fn(result));
        });
        return p;
    }
    _resolve(result) {
        this._thenFns.forEach(fn => fn(result));
    }
}

new Promisify((resolve) => {
    setTimeout(() => resolve(1), 3);
}).then(n => n + 1).then(n => n + 6).then(n => console.log(n))

