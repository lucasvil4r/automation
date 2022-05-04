import pyautogui
import time

# Coleta CFOP
cfop = pyautogui.confirm(text='Qual CFOP deseja lançar ?', title='Selecione CFOP', buttons=['1353', '2353'])
pyautogui.alert(text='IMPORTANTE PARA USO INICIAL DO'
                     ' PROGRAMA:\n\nCertifique que aba "emissão de notas fiscais esteja aberta e apenas os aquivos para lançamento se encontre na aréa de trabalho".',title='ATENÇÃO', button='OK')

loop = 'Continuar lançando'
while (loop == 'Continuar lançando'):

    ddl = pyautogui.prompt(text='Selecione para quantos dias CT-e foi faturado:', title='Pagamentos:', default='')

    pyautogui.PAUSE = 0.200

# Seleciona tipo de operação\n",

    pyautogui.click(x=1925, y=379)

# Seleciona acão\n",

    pyautogui.click(x=2281, y=371)

# Seleciona tipo nota fiscal\n",

    pyautogui.click(x=2242, y=363)
    pyautogui.click(x=2194, y=471)

    pyautogui.click(x=2024, y=468)

    if (cfop == "1353"):
        pyautogui.press('enter')
    else:
        pyautogui.write('2353')
        pyautogui.press('enter')
        pyautogui.press('enter')

# Executa NF\n",

    pyautogui.click(x=2323, y=518)
    time.sleep(1.5)

# Seleciona XML e PDF
    pyautogui.press('tab')
    pyautogui.press('f4')
    pyautogui.hotkey('shift', 'f6')
    pyautogui.hotkey('shift', 'f6')
    pyautogui.press('pageup')
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('f4')
    pyautogui.hotkey('shift', 'f6')
    pyautogui.hotkey('shift', 'f6')
    pyautogui.press('pageup')
    pyautogui.press('enter')

# Seleciona fornecedor
    pyautogui.press('tab')
    pyautogui.press('f4')
    pyautogui.press('enter')

# Importa XML

    pyautogui.click(x=2190, y=650)

# corrige erro do sistema

    pyautogui.alert(text='Precione "OK" SOMENTE após aba cadastro de notas ficais abrir, as vezes ocorre um erro ao acessar essa aba corriga manualmente ESPERE ABRIR e precione "OK".',title='ATENÇÃO', button='OK')

# Copia data de entrada com a de emissão\n",
    pyautogui.press('tab', presses=4, interval=0.100)
    pyautogui.hotkey('ctrl', "c")
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', "v")

# input ddl
    pyautogui.press('tab', presses=8, interval=0.100)
    pyautogui.write(ddl)
    pyautogui.press('enter')

# Seleciona aba total das duplicadas\n"
    pyautogui.click(x=2152, y=356)

# Gera duplicata\n",
    pyautogui.press('tab')
    pyautogui.press('enter')

# FinalizarNota\n",
    pyautogui.alert(text='CONFERIR DATA DE VENCIMENTO, CASO ESTEJA EM DESACORDO ALTERE DDL MANUALMENTE E LOGO APÓS PRESSIONE "OK" E A NOTA SERÁ FINALIZADA.', title='CONFERIR', button='OK')
    pyautogui.click(x=1769, y=687)
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.click(x=1925, y=379)

# Seleciona acão\n",

    #pyautogui.click(x=2281, y=371)

# Seleciona tipo nota fiscal\n",

    #pyautogui.click(x=2242, y=363)
    #pyautogui.click(x=2194, y=471)
    pyautogui.click(x=2024, y=468)

# Seleciona CFOP\n",

    if (cfop == "1353"):
        pyautogui.press('enter')
    else:
        pyautogui.write('2353')
        pyautogui.press('enter')
        pyautogui.press('enter')

# Executa NF\n",

    pyautogui.click(x=2359, y=519)
    time.sleep(2)

# Apagar XML e PDF LANÇADO
    pyautogui.press('tab')
    pyautogui.press('f4')
    pyautogui.hotkey('shift', 'f6')
    pyautogui.hotkey('shift', 'f6')
    pyautogui.press('pageup')
    pyautogui.press('delete')
    pyautogui.press('tab', presses=5, interval=0.500)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('f4')
    pyautogui.hotkey('shift', 'f6')
    pyautogui.hotkey('shift', 'f6')
    pyautogui.press('pageup')
    pyautogui.press('delete')
    pyautogui.press('tab', presses=5, interval=0.500)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'f4')
    pyautogui.press('enter')
    loop = pyautogui.confirm(text='Deseja lançar outro CT-e', title='CONTINAR LANÇAMENTO', buttons=['Continuar lançando', 'Finalizar'])
else:
    pyautogui.alert(text='Até logo...', title='FINALIZADO', button='OK')
