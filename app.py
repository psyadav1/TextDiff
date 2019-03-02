#!flask/bin/python
from flask import Flask, jsonify, request
import diff_match_patch as dmp_module

app = Flask(__name__)

dmp = dmp_module.diff_match_patch()


@app.route('/text-diff', methods=['POST'])
def text_diff():
    if not request.json or 'text_from' not in request.json or 'text_to' not in request.json:
        return jsonify({'error': 'No content of request.json!'}), 400
    diff = dmp.diff_main(request.json['text_from'], request.json['text_to'])
    return jsonify({'data': diff}), 201


@app.route('/text-diff-cleanup-semantic', methods=['POST'])
def text_diff_cleanup_semantic():
    if not request.json or 'text_from' not in request.json or 'text_to' not in request.json:
        return jsonify({'error': 'No content of request.json!'}), 400
    diff = dmp.diff_main(request.json['text_from'], request.json['text_to'])
    dmp.diff_cleanupSemantic(diff)
    return jsonify({'data': diff}), 201


if __name__ == '__main__':
    app.run(debug=True)
