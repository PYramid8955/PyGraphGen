def GenSvg(data:list) -> str:
    vb = max([max(data), len(data)]) # viewBox
    svg = f'<?xml version="1.0" encoding="utf-8"?><svg viewBox="0 0 {vb} {vb}" xmlns="http://www.w3.org/2000/svg"><path d="' # "
    add = vb/max(data) # x background lines
    for i in range(max(data)):
        svg += f'M0,{i*add}l{vb},0'
    svg += f'" stroke="black" stroke-width="{0.001*vb}"/><path d="' # "
    add = vb/len(data) # y background lines
    lineWidth = add*0.216/100 * vb
    for i in range(len(data)):
        svg += f'M{i*add},0l0,{vb}'
    svg += f'" stroke="black" stroke-width="{0.001*vb}"/><path d="M0,{vb}L' # "
    for i in range(len(data)):
        svg += f'{(i+1)*add},{vb-data[i]} '   
    svg += f'" stroke="#ff0000" stroke-width="{lineWidth}" fill="none" /><path d="M0,0l0,{vb}l{vb},0.0" fill="none" stroke="#000c7a" stroke-width="{lineWidth*2}"/><circle cx="0" cy="{vb}" fill="yellow" r="{lineWidth*2}"/></svg>'
    return svg
