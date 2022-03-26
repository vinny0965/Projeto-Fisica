'''
  __  __  _____     _____ __  __ _____ _   _ _____ ___    ____  _____ _____ ___ _      __ _   _ _____ ___  
 |  \/  |/ _ \ \   / /_ _|  \/  | ____| \ | |_   _/ _ \  |  _ \| ____|_   _|_ _| |    /_/| \ | | ____/ _ \ 
 | |\/| | | | \ \ / / | || |\/| |  _| |  \| | | || | | | | |_) |  _|   | |  | || |   |_ _|  \| |  _|| | | |
 | |  | | |_| |\ V /  | || |  | | |___| |\  | | || |_| | |  _ <| |___  | |  | || |___ | || |\  | |__| |_| |
 |_|  |_|\___/  \_/  |___|_|  |_|_____|_| \_| |_| \___/  |_| \_\_____| |_| |___|_____|___|_| \_|_____\___/  0.2.1

'''                                                                                                        
from vpython import *

class RectilinearMovement:
    def __init__(self) -> None:
        self.WIDTH = 1400
        self.setInitialValues()
        self.createObjects()
        self.createWidgets()
        self.createGraph()
        self.updateGraphs()

    '''
        ┌─┐┬ ┬┌┐┌┌─┐┌─┐┌─┐┌─┐  ┌┬┐┌─┐  ┌─┐┬─┐┬┌─┐┌─┐┌─┐┌─┐
        ├┤ │ │││││  │ │├┤ └─┐   ││├┤   │  ├┬┘│├─┤│  ├─┤│ │
        └  └─┘┘└┘└─┘└─┘└─┘└─┘  ─┴┘└─┘  └─┘┴└─┴┴ ┴└─┘┴ ┴└─┘
    '''

    def setInitialValues(self):
        # definição dos valores iniciais
        self.t  = 0
        self.dt = .01
        self.a  = vector(0,0,0)
        self.object_vel = vector(0,0,0)
        self.running    = False
        # self.isInitial  = True
        # self.initial_vel = vector(0,0,0)
        # self.initial_pos = vector(0,0,0)

    def createObjects(self):
        # esfera
        self.object = sphere(pos = vector(0,1,0), radius = 1, color = color.red)
        
        # criação e configuração da seta de aceleração [alterar para a develocidade]
        self.ace_arrow_right = arrow(pos = vector((self.object.pos.x-self.object.radius)/2, self.object.pos.y + 2, self.object.pos.z))
        
        self.ace_arrow_right.visible = False
        
        self.ace_arrow_left = arrow(pos = vector((self.object.pos.x-self.object.radius)/2, self.object.pos.y + 2, self.object.pos.z))
        self.ace_arrow_left.rotate(180,vector(0,0,0))
        
        self.ace_arrow_left.visible = False
        
        # chão abaixo da esfera
        self.ground = box(pos = vector(0,0,0), size = vector(200,.5,2), color = color.white)
        
        # largura da cena
        scene.width = self.WIDTH
        
        # configurar camera para seguir esfera
        scene.follow(self.object)

    def createWidgets(self):
        # vSpace() -> espaço na vertical
        # hSpace() -> espaço na horizontal
        self.vSpace(1)
       
        # texto velocidade
        self.velocity_label = wtext(text = "Velocidade:")
        self.hSpace(2)
       
        # caixa de texto para a inserção da velocidade
        self.velocity_input = winput(bind = self.nothing, type = "numeric", width = 100, _height = 20)
        self.hSpace(3)
       
        # texto acereleração
        self.aceleration_label = wtext(text = "Aceleração:")
        self.hSpace(2)
       
        # caixa de texto para a inserção da aceleração
        self.aceleration_input = winput(bind = self.nothing, type = "numeric", width = 100, _height = 20)
        self.hSpace(3)
        
        # botão de iniciar a animação junto com os graficos
        self.run_button = button(bind = self.move, text = "Executar")
        self.hSpace(3)

        # botão para reiniciar todos os valores
        self.reset_button = button(bind = self.reset, text = "Resetar")
        self.hSpace(5)
       
        # texto "Posição X = "
        self.x_pos_label = wtext(text = "Posição X = ")
        self.hSpace(1)
        
        # texto informando a posição X em tempo real
        self.x_pos_info = wtext(text = self.object.pos.x)
        self.hSpace(3)
        
        # texto "Tempo = "
        self.time_label = wtext(text = "Tempo = ")
        self.hSpace(1)
        
        # texto informando a o tempo em tempo real
        self.time_info = wtext(text = self.t)
        self.vSpace(1)

        wtext(text = " ")
        self.vSpace(1)

    '''
        ┌─┐┬ ┬┌┐┌┌─┐┌─┐┌─┐┌─┐  ┌┬┐┌─┐  ┌─┐┌─┐┬  ┌─┐┬ ┬┬  ┌─┐┌─┐
        ├┤ │ │││││  │ │├┤ └─┐   ││├┤   │  ├─┤│  │  │ ││  │ │└─┐
        └  └─┘┘└┘└─┘└─┘└─┘└─┘  ─┴┘└─┘  └─┘┴ ┴┴─┘└─┘└─┘┴─┘└─┘└─┘
    '''

    def move(self):
        
        # captura a velocidade informada pelo usuario
        self.object_vel.x = float((self.velocity_input.text))
        
        # captura a aceleração informada pelo usuario
        self.a.x = float((self.aceleration_input.text))
        
        # aumenta o valor x do grafico 2 | 5 posições a mais do valor maximo informado
        if self.object_vel.x > self.graph2_config.xmax:
            self.graph2_config.xmax = self.object_vel.x + 5

        # aumenta o valor x do grafico 3 | 5 posições a mais do valor maximo informado
        if self.a.x > self.graph3_config.xmax:
            self.graph3_config.xmax = self.a.x + 5

        # armazena apenas os valores iniciais
        # if self.isInitial:
        #     self.initial_vel = self.object_vel.x
        #     self.initial_pos = self.object.pos
        #     self.isInitial   = False

        self.running = True
        while self.running:
            # fps
            rate(300)

            # calculo do tempo
            self.t = self.t + self.dt

            # calculo da aceleração
            # self.a = (self.object_vel.x - self.initial_vel) / (self.object.pos.x - self.initial_pos)
            
            # calculo da posição
            self.object.pos.x = self.object.pos.x + (self.object_vel.x * self.dt)
            # self.object.pos.x = (self.a.x * (self.t**2)) / 2

            # dobra o tamanho do chão quando a esfere está proxima do fim
            if self.object.pos.x > self.ground.size.x // 2 or self.object.pos.x < -(self.ground.size.x // 2) :
                self.ground.size.x = self.ground.size.x * 2

            # atualiza as informações que aparecem na tela
            self.updateScreenInfo()

            # atualiza as setas
            self.updateArrows()

            # atualiza os graficos
            self.updateGraphs()

    def updateArrows(self):
        self.ace_arrow_right.pos.x = self.object.pos.x
        self.ace_arrow_left.pos.x = self.object.pos.x
        
        if self.object_vel.x == 0:
            self.ace_arrow_right.visible = False
            self.ace_arrow_left.visible  = False
        elif self.object_vel.x>0:
            self.ace_arrow_right.visible = True
            self.ace_arrow_left.visible  = False
        else:
            self.ace_arrow_right.visible = False
            self.ace_arrow_left.visible  = True

    def updateScreenInfo(self):
        self.x_pos_info.text = self.object.pos.x
        self.time_info.text  = self.t
   
    '''
        ┌─┐┬ ┬┌┐┌┌─┐┌─┐┌─┐┌─┐  ┌┬┐┌─┐  ┌─┐┬─┐┌─┐┌─┐┬┌─┐┌─┐┌─┐
        ├┤ │ │││││  │ │├┤ └─┐   ││├┤   │ ┬├┬┘├─┤├┤ ││  │ │└─┐
        └  └─┘┘└┘└─┘└─┘└─┘└─┘  ─┴┘└─┘  └─┘┴└─┴ ┴└  ┴└─┘└─┘└─┘
    '''

    def createGraph(self):
        # grafico 1 posição / tempo
        self.graph1_config = graph(width = self.WIDTH, _height = 400, title = 'Posição / Tempo', xtitle = 'Tempo', ytitle = 'Posição', foreground = color.black, background = color.orange, fast = True)
        self.graph1 = gcurve(graph = self.graph1_config, color = color.red)
    
        # grafico 2 velocidade / tempo
        self.graph2_config = graph(width = self.WIDTH, _height = 400, title = 'Velocidade / Tempo', xtitle = 'Tempo', ytitle = 'Velocidade', foreground = color.black, background = color.yellow, fast = False, scroll = True, xmin = 0, xmax = 10)
        self.graph2 = gcurve(graph = self.graph2_config, color = color.blue)

        # grafico 3 aceleração / tempo
        self.graph3_config = graph(width = self.WIDTH, _height = 400, title = 'Aceleração / Tempo', xtitle = 'Tempo', ytitle = 'Aceleração', foreground = color.black, background = color.cyan, fast = False, scroll = True, xmin = 0, xmax = 5)
        self.graph3 = gcurve(graph = self.graph3_config, color = color.black)
 
    def updateGraphs(self):
        self.graph1.plot(self.t, self.object.pos.x)
        self.graph2.plot(self.t, self.object_vel.x)
        self.graph3.plot(self.t, self.a.x)

    '''
        ┬ ┬┬ ┌┬┐┬┬  ┬┌┬┐┌─┐┬─┐┬┌─┐┌─┐
        │ ││  │ ││  │ │ ├─┤├┬┘││ │└─┐
        └─┘┴─┘┴ ┴┴─┘┴ ┴ ┴ ┴┴└─┴└─┘└─┘
    '''

    def vSpace(self, times):
        # espaço na vertical
        scene.append_to_caption(f'\n' * times)

    def hSpace(self, times):
        # espaço na horizontal
        scene.append_to_caption(f' ' * times)

    def reset(self):
        # reseta todos os valores
        self.setInitialValues()
        self.updateGraphs()

    def nothing(self):
        # literalmente nada
        pass

RectilinearMovement()