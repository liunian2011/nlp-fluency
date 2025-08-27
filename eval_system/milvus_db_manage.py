from pymilvus import connections, utility
from pymilvus import FieldSchema, CollectionSchema, DataType, Collection
#import faiss
#import random
#import numpy as np
from emb_util import get_text_vectors
from tqdm import tqdm

# 连接 Milvus 服务
connections.connect("default", host="10.200.49.1", port="9092")




def insert_data_demo():
    import faiss
    # 定义字段
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=False),
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=384),
        FieldSchema(name="name", dtype=DataType.VARCHAR, max_length=50)
    ]

    schema = CollectionSchema(fields, description="example collection")

    # 创建 Collection
    collection = Collection(name="demo_collection", schema=schema)

    #ids = [i for i in range(10)]
    #index = faiss.read_index("./geo_store/geo_knowledge.index")
    #vectors = [[random.random() for _ in range(384)] for _ in range(10)]
    #names = [f"name_{i}" for i in range(10)]

    faiss_index = faiss.read_index("./geo_store/geo_knowledge.index")
    # 获取向量总数和维度
    ntotal = faiss_index.ntotal
    d = faiss_index.d
    print(f"向量总数: {ntotal}, 维度: {d}")

    vectors = faiss_index.reconstruct_n(0, ntotal)  # 返回 numpy.ndarray
    ids = list(range(ntotal))
    vectors_list = vectors.tolist()
    names = [f"vec_{i}" for i in range(ntotal)]

    # 插入
    collection.insert([ids, vectors_list, names])
    collection.flush()

    # 为 vector 字段创建索引
    index_params = {
        "metric_type": "L2",  # 相似度度量方法，可选 IP（内积）、COSINE 等
        "index_type": "IVF_FLAT",  # 索引类型，可选 IVF_FLAT, IVF_SQ8, HNSW 等
        "params": {"nlist": 128}   # 索引参数，nlist 越大精度越高但速度可能慢
    }

    collection.create_index(
        field_name="vector",
        index_params=index_params
    )
    collection.load()


def insert_text_to_milvus(text_list):
    import faiss
    # 定义字段
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=384),
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535)
    ]

    schema = CollectionSchema(fields, description="geoscience text")

    # 创建 Collection
    collection = Collection(name="geography", schema=schema)

    vectors_list = []
    insert_text_list = []
    for text in tqdm(text_list):
        vector = get_text_vectors(text)
        vectors_list.append(vector)

        insert_text = text[0:60000]
        insert_text_list.append(insert_text)

    try:
        # 插入
        # collection.insert([vectors_list, insert_text_list])
        #分批插入
        batch_size = 200
        for i in range(0, len(vectors_list), batch_size):
            vectors_batch = vectors_list[i: i+batch_size]
            insert_text_batch = insert_text_list[i: i+batch_size]
            collection.insert([vectors_batch, insert_text_batch])
        collection.flush()
    except Exception as e:
        print(f'write data error:{e}')


    # 为 vector 字段创建索引
    index_params = {
        "metric_type": "L2",  # 相似度度量方法，可选 IP（内积）、COSINE 等
        "index_type": "IVF_FLAT",  # 索引类型，可选 IVF_FLAT, IVF_SQ8, HNSW 等
        "params": {"nlist": 128}   # 索引参数，nlist 越大精度越高但速度可能慢
    }

    collection.create_index(
        field_name="vector",
        index_params=index_params
    )
    collection.load()



def search_data(search_text):
    # search_text = 'significantly influenced by both clouds and Earth’s surface temperature (EST)'
    # search_text = """Flying A was one of the first motion pictures studios in California history. On August 12, 2011, a plaque was unveiled on the Wolff building at Third Avenue and La Mesa Boulevard commemorating Dwan and the Flying A Studios origins in La Mesa, California.\nAfter making a series of westerns and comedies, Dwan directed fellow Canadian-American Mary Pickford in several very successful movies as well as her husband, Douglas Fairbanks, notably in the acclaimed 1922 Robin Hood. Dwan directed Gloria Swanson in eight feature films, and one short film made in the short-lived sound-on-film process Phonofilm."""
    # search_text = """## Early life\n\nBorn Joseph Aloysius Dwan in Toronto, Ontario, Canada, Dwan was the younger son of commercial traveler of woolen clothing Joseph Michael Dwan (1857–1917) and his wife Mary Jane Dwan, née Hunt. The family moved to the United States when he was seven years old on December 4, 1892, by ferry from Windsor to Detroit, according to his naturalization petition of August 1939. His elder brother, Leo Garnet Dwan (1883–1964), became a physician.\nAllan Dwan studied engineering at the University of Notre Dame and then worked for a lighting company in Chicago. He had a strong interest in the fledgling motion picture industry, and when Essanay Studios offered him the opportunity to become a scriptwriter, he took the job. At that time, some of the East Coast movie makers began to spend winters in California where the climate allowed them to continue productions requiring warm weather. Soon, a number of movie companies worked there year-round, and in 1911, Dwan began working part-time in Hollywood. While still in New York, in 1917 he was the founding president of the East Coast chapter of the Motion Picture Directors Association.\n\n## Career\n\nDwan started his directing career by accident in 1911, when he was sent by his employers to California, in order to locate a company that had vanished. Dwan managed to track the company down, and learned that they were waiting for the film's director (who was an alcoholic) to return from a binge (and allowing them to return to work). Dwan wired back to his employers in Chicago, informing them of the situation, and suggested that they disband the company. They wired back, instructing Dwan to direct the film. When Dwan informed the company of the situation, and that their jobs were on the line, they responded: \"You're the best damn director we ever saw\".\nDwan operated Flying A Studios in La Mesa, California, from August 1911 to July 1912. Flying A was one of the first motion pictures studios in California history. On August 12, 2011, a plaque was unveiled on the Wolff building at Third Avenue and La Mesa Boulevard commemorating Dwan and the Flying A Studios origins in La Mesa, California.\nAfter making a series of westerns and comedies, Dwan directed fellow Canadian-American Mary Pickford in several very successful movies as well as her husband, Douglas Fairbanks, notably in the acclaimed 1922 Robin Hood. Dwan directed Gloria Swanson in eight feature films, and one short film made in the short-lived sound-on-film process Phonofilm. This short, also featuring Thomas Meighan and Henri de la Falaise, was produced as a joke, for the April 26, 1925 \"Lambs' Gambol\" for The Lambs, with the film showing Swanson crashing the all-male club.\nFollowing the introduction of the talkies, Dwan directed child-star Shirley Temple in Heidi (1937) and Rebecca of Sunnybrook Farm (1938).\nDwan helped launch the career of two other successful Hollywood directors, Victor Fleming, who went on to direct The Wizard of Oz and Gone With the Wind, and Marshall Neilan, who became an actor, director, writer and producer. Over a long career spanning almost 50 years, Dwan directed 125 motion pictures, some of which were highly acclaimed, such as the 1949 box office hit, Sands of Iwo Jima. He directed his last movie in 1961.\nBeing one of the last surviving pioneers of the cinema, he was interviewed at length for the 1980 documentary series Hollywood.\nHe died in Los Angeles at the age of 96, and is interred in the San Fernando Mission Cemetery, Mission Hills, California.\nDwan has a star on the Hollywood Walk of Fame at 6263 Hollywood Boulevard.\nDaniel Eagan of Film Journal International described Dwan as one of the early pioneers of cinema, stating that his style \"is so basic as to seem invisible, but he treats his characters with uncommon sympathy and compassion.\"\n\n## Partial filmography as director\n\n*The Restless Spirit (1913)\n*Back to Life (1913)\n*Bloodhounds of the North (1913)\n*The Lie (1914)\n*The Honor of the Mounted (1914)\n* The Unwelcome Mrs. Hatch (1914)\n*Remember Mary Magdalen (1914)\n*Discord and Harmony (1914)\n*The Embezzler (1914)\n*The Lamb, the Woman, the Wolf (1914)\n*The End of the Feud (1914)\n*The Test (1914) (*writer)\n*The Tragedy of Whispering Creek (1914)\n*The Unlawful Trade (1914)\n*The Forbidden Room (1914)\n*The Hopes of Blind Alley (1914)\n*Richelieu (1914)\n* Wildflower (1914)\n*A Small Town Girl (1915)\n*David Harum (1915)\n*A Girl of Yesterday (1915)\n*The Pretty Sister of Jose (1915)\n* Jordan Is a Hard Road (1915)\n*The Habit of Happiness (1916)\n*The Good Bad Man (1916)\n*An Innocent Magdalene (1916)\n*The Half-Breed (1916)\n*Manhattan Madness (1916)\n*Accusing Evidence (1916)\n*Panthea (1917)\n*A Modern Musketeer (1917)\n*Bound in Morocco (1918)\n*Headin' South (1918)\n*Mr. Fix-It (1918)\n*He Comes Up Smiling (1918)\n*Cheating Cheaters (1919)\n*The Dark Star (1919)\n*Getting Mary Married (1919)\n*Soldiers of Fortune (1919)\n*In The Heart of a Fool (1920) also producer\n*The Forbidden Thing (1920) also producer\n*A Splendid Hazard (1920)\n*A Perfect Crime (1921)\n* The Sin of Martha Queed (1921)\n* A Broken Doll (1921)\n*Robin Hood (1922)\n*Zaza (1923)\n*Big Brother (1923)\n*Manhandled (1924)\n*Argentine Love (1924)\n*The Coast of Folly (1925)\n*Night Life of New York (1925)\n*Stage Struck (1925)\n*Padlocked (1926)\n*Sea Horses (1926)\n*Summer Bachelors (1926)\n*Tin Gods (1926)\n*French Dressing (1927)\n*The Joy Girl (1927)\n*East Side, West Side (1927)\n*The Big Noise (1928)\n*Frozen Justice (1929)\n*The Iron Mask (1929)\n*Tide of Empire (1929)\n*The Far Call (1929)\n*What a Widow! (1930)\n*Man to Man (1930)\n*Wicked (1931)\n*While Paris Sleeps (1932)\n*Counsel's Opinion (1933)\n*Black Sheep (1935)\n*Navy Wife (1935)\n*High Tension (1936)\n*15 Maiden Lane (1936)\n*One Mile from Heaven (1937)\n*Heidi (1937)\n*Rebecca of Sunnybrook Farm (1938)\n*Suez (1938)\n* Josette (1938)\n*The Three Musketeers (1939)\n*The Gorilla (1939)\n*Frontier Marshal (1939)\n*Sailor's Lady (1940)\n*Young People (1940)\n*Trail of the Vigilantes (1940)\n*Look Who's Laughing (1941) also producer\n*Rise and Shine (1941)\n*Friendly Enemies (1942)\n*Around the World (1943) also producer\n*Up in Mabel's Room (1944)\n*Abroad with Two Yanks (1944)\n*Getting Gertie's Garter (1945) also screenwriter\n*Brewster's Millions (1945)\n*Rendezvous with Annie (1946)\n*Driftwood (1947)\n*Calendar Girl (1947)\n*Northwest Outpost (1947) also associate producer\n*The Inside Story (1948)\n*Angel in Exile (1948) (with Philip Ford)\n*Sands of Iwo Jima (1949)\n*Surrender (1950)\n*Belle Le Grand (1951)\n*Wild Blue Yonder (1951)\n*I Dream of Jeanie (1952)\n*Montana Belle (1952)\n*Woman They Almost Lynched (1953)\n* Sweethearts on Parade (1953)\n*Silver Lode (1954)\n*Passion (1954)\n*Cattle Queen of Montana (1954)\n*Tennessee's Partner (1955)\n*Pearl of the South Pacific (1955)\n*Escape to Burma (1955)\n*Slightly Scarlet (1956)\n*Hold Back the Night (1956)\n*The Restless Breed (1957)\n*The River's Edge (1957)\n*Enchanted Island (1958)\n*Most Dangerous Man Alive (1961)"""
    search_vector = get_text_vectors(search_text)
    #print(f'search vector len:{len(search_vector)}')

    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=384),
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535)
    ]
    schema = CollectionSchema(fields, description="geoscience text")

    # 创建 Collection
    collection = Collection(name="geography", schema=schema)

    results = collection.search(
        data=[search_vector],
        anns_field="vector",
        param={"metric_type": "L2", "params": {"nprobe": 10}},
        limit=1,
        output_fields=["text"]
    )



    return results



def main():
    #coll = insert_data_demo()
    try:
        search_data()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()