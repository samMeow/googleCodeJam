const fs = require('fs');

function groupBy(func, ar) {
    return ar.reduce((memo, x) => ({
        ...memo,
        [func(x)]: [ x, ...(memo[func(x)] || [])]
    }), {})
}

function makeTree(words, depth) {
    if (words.length > 2) {
        const subtree = groupBy(x => x[depth] || 'null', words);
        return Object.entries(subtree).reduce((memo, [k, v]) => ({
            ...memo,
            [k]: k === 'null' ? v : makeTree(v, depth + 1)
        }), {})
    }
    return words
}

function getCount(tree) {
    if (Array.isArray(tree)) {
        if (tree.length >= 2) {
            return { buf: tree.length - 2, count: 1 };
        }
        return { buf: 1, count: 1 };
    }
    return Object.values(tree).reduce((memo, node) => {
        if (Array.isArray(node)) {
            if (node.length >= 2) {
                memo.count = memo.count + 1;
                memo.buf += node.length - 2;
            } else {
                memo.buf += node.length;
            }
            return memo;
        }
        const { buf, count } = getCount(node);
        memo.count += count;
        memo.buf += buf;
        if (buf >= 2) {
            memo.count += 1;
            memo.buf -= 2;
        }
        return memo;
    }, { buf: 0, count: 0, grouped: false });
}

function solve(problem) {
    const words = problem.map(x => x.split('').reverse().join(''))

    const tree = makeTree(words, 0)
    const {buf, count} = getCount(tree)
    // console.log(buf, count)
    return count * 2;
    // console.log(JSON.stringify(tree, null, 2))
}

async function read(stream) {
    let buffer = Buffer.alloc(0);
    for await (const chunk of stream) {
        buffer = Buffer.concat([buffer, chunk]);
    }
    return buffer.toString('utf8');
}

async function main() {
    const input = await read(process.stdin);
    const data = input.split('\n');
    const [_, ...rest] = data;
    
    const problems = []
    let buf = []
    data.forEach(x => {
        const num = parseInt(x);
        if (num > 0) {
            if (buf.length !== 0) {
                problems.push(buf)
                buf = []
            }
        } else {
            if (x.length > 0) buf.push(x)
        }
    })
    problems.push(buf);
    
    problems.forEach((pro, idx) => {
        const count = solve(pro);
        console.log(`Case #${idx+1}: ${count}`);
    })

}

main();
