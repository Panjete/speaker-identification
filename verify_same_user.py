import nemo.collections.asr as nemo_asr

speaker_model = nemo_asr.models.EncDecSpeakerLabelModel.from_pretrained("nvidia/speakerverification_en_titanet_large")


def verify_same_user(s, h):
    decision = speaker_model.verify_speakers(s, h)
    if decision:
        print("The same user")
    else:
        print("Different users")
    return decision

if __name__ == "__main__":
    verify_same_user("manual_data/proc/s.wav","manual_data/proc/hello.wav")