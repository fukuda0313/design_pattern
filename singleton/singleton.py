# シングルトンクラスの定義
class Singleton:
    # インスタンス変数
    _instance = None

    # __new__メソッドの実装
    def __new__(cls):
        # NotImplementedErrorを発生させる
        raise NotImplementedError('initialized error')

    # 内部の__new__メソッドを呼び出すクラスメソッド
    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    # インスタンスを取得するクラスメソッド
    @classmethod
    def get_instance(cls):
        # インスタンスが存在しない場合、新しいインスタンスを作成する
        if not cls._instance:
            cls._instance = cls.__internal_new__()
        return cls._instance
