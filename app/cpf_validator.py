from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def valida_cpf(cpf):
    cpf = ''.join(re.findall(r'\d', str(cpf)))
    
    if len(cpf) != 11:
        return False
    
    if cpf == cpf[::-1]:
        return False
    
    for i in range(9, 11):
        value = sum(int(a) * b for a, b in zip(cpf[:i], range(i + 1, 1, -1)))
        digit = 11 - value % 11
        if digit > 9:
            digit = 0
        if str(digit) != cpf[i]:
            return False
    return True

@app.route('/valida_cpf', methods=['POST'])
def valida_cpf_route():
    content = request.json
    cpf = content.get('cpf', '')
    
    is_valid = valida_cpf(cpf)
    
    return jsonify({"cpf": cpf, "valido": is_valid})

if __name__ == '__main__':
    app.run(debug=True)

