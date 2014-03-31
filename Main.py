from game import Game


class GameApp():
    @staticmethod
    def main():
        game = Game()
        game.start()

if __name__ == '__main__':
    GameApp.main()
